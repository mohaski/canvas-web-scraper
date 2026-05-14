import os
import re
import asyncio
from datetime import datetime

from dotenv import load_dotenv
from playwright.async_api import async_playwright
from bs4 import BeautifulSoup
from markdownify import markdownify as md
from firecrawl import FirecrawlApp

# =========================================================
# CONFIGURATION
# =========================================================

load_dotenv()

BASE_URL = "https://moringa.instructure.com"
COURSE_ID = "1391"

HEADLESS = False

DATA_DIR = "data"

FIRECRAWL_API_KEY = os.getenv("FIRECRAWL_API_KEY")

# Optional Firecrawl enhancement
firecrawl_app = None

if FIRECRAWL_API_KEY:
    firecrawl_app = FirecrawlApp(
        api_key=FIRECRAWL_API_KEY
    )

# =========================================================
# SKIP LIST
# =========================================================

SKIP_LIST = [
    "Student Contract",
    "Data Policy",
    "Media Consent Form",
    "Student Handbook",
    "Student Resources",
    "Moringa School Emergency Policy and Procedure"
]

# =========================================================
# HELPERS
# =========================================================

def sanitize_name(name):
    """
    Remove invalid filename characters.
    """

    return re.sub(
        r'[<>:"/\\|?*]',
        '',
        name
    ).strip()


def ensure_absolute_url(url):
    """
    Convert relative URLs to absolute URLs.
    """

    if not url:
        return url

    if url.startswith("http"):
        return url

    return f"{BASE_URL}{url}"


async def save_markdown(
    content,
    folder_path,
    filename,
    order_index
):
    """
    Save markdown file preserving scrape order.
    """

    os.makedirs(folder_path, exist_ok=True)

    clean_filename = sanitize_name(filename)

    numbered_filename = (
        f"{order_index:02d}_{clean_filename}.md"
    )

    filepath = os.path.join(
        folder_path,
        numbered_filename
    )

    with open(
        filepath,
        "w",
        encoding="utf-8"
    ) as f:

        f.write(content)

    print(f"✅ Saved: {filepath}")


# =========================================================
# INLINE MEDIA PRESERVATION
# =========================================================

def preserve_media_inline(soup):
    """
    Replace media elements with markdown-compatible
    inline placeholders BEFORE markdown conversion.
    """

    # -----------------------------------------------------
    # IMAGES
    # -----------------------------------------------------

    for img in soup.find_all("img"):

        src = img.get("src")

        if not src:
            continue

        src = ensure_absolute_url(src)

        alt = img.get("alt", "image")

        markdown_img = (
            f"\n\n![{alt}]({src})\n\n"
        )

        img.replace_with(markdown_img)

    # -----------------------------------------------------
    # IFRAMES (YouTube/Vimeo/Canvas Studio)
    # -----------------------------------------------------

    for iframe in soup.find_all("iframe"):

        src = iframe.get("src")

        if not src:
            continue

        src = ensure_absolute_url(src)

        video_text = (
            f"\n\n[VIDEO LINK]({src})\n\n"
        )

        iframe.replace_with(video_text)

    # -----------------------------------------------------
    # HTML5 VIDEOS
    # -----------------------------------------------------

    for video in soup.find_all("video"):

        src = video.get("src")

        # fallback to source tag
        if not src:

            source = video.find("source")

            if source:
                src = source.get("src")

        if not src:
            continue

        src = ensure_absolute_url(src)

        video_text = (
            f"\n\n[VIDEO LINK]({src})\n\n"
        )

        video.replace_with(video_text)

    return soup


# =========================================================
# ATTACHMENT EXTRACTION
# =========================================================

def extract_attachments(soup):

    attachments = []

    allowed_extensions = [
        ".pdf",
        ".doc",
        ".docx",
        ".ppt",
        ".pptx",
        ".zip",
        ".csv",
        ".xlsx",
        ".txt"
    ]

    for a in soup.find_all("a", href=True):

        href = a["href"]

        if any(
            ext in href.lower()
            for ext in allowed_extensions
        ):

            attachments.append({
                "name": a.get_text(strip=True),
                "url": ensure_absolute_url(href)
            })

    return attachments


# =========================================================
# CLEAN CANVAS HTML
# =========================================================

def clean_canvas_html(soup):
    """
    Remove Canvas UI junk.
    """

    # Remove scripts/styles
    for tag in soup([
        "script",
        "style",
        "noscript"
    ]):
        tag.decompose()

    # Remove unnecessary Canvas UI
    selectors_to_remove = [
        ".header-bar",
        ".navigation",
        ".breadcrumbs",
        ".module-sequence-footer",
        ".course-title",
        ".ic-app-nav-toggle-and-crumbs"
    ]

    for selector in selectors_to_remove:

        for el in soup.select(selector):
            el.decompose()

    return soup


# =========================================================
# MARKDOWN BUILDER
# =========================================================

def build_enriched_markdown(
    title,
    markdown_content,
    attachments,
    source_url
):

    final_md = f"# {title}\n\n"

    final_md += markdown_content.strip()

    # -----------------------------------------------------
    # ATTACHMENTS
    # -----------------------------------------------------

    if attachments:

        final_md += (
            "\n\n---\n\n"
            "# Attachments\n\n"
        )

        for attachment in attachments:

            final_md += (
                f"- {attachment['name']}: "
                f"{attachment['url']}\n"
            )

    # -----------------------------------------------------
    # SOURCE INFORMATION
    # -----------------------------------------------------

    final_md += (
        "\n\n---\n\n"
        "# Source Information\n\n"
    )

    final_md += (
        f"Original URL: {source_url}\n\n"
    )

    final_md += (
        f"Scraped At: "
        f"{datetime.now().isoformat()}\n"
    )

    return final_md


# =========================================================
# FIRECRAWL ENHANCEMENT
# =========================================================

def try_firecrawl(url):

    if not firecrawl_app:
        return None

    try:

        result = firecrawl_app.scrape_url(
            url,
            params={
                "formats": ["markdown"]
            }
        )

        # Object response
        if hasattr(result, "markdown"):
            return result.markdown

        # Dictionary response
        if isinstance(result, dict):
            return result.get("markdown")

    except Exception as e:

        print(f"⚠️ Firecrawl failed: {e}")

    return None


# =========================================================
# SCRAPE SINGLE PAGE
# =========================================================

async def scrape_page(
    context,
    page_title,
    page_url,
    folder_path,
    item_index
):

    full_url = ensure_absolute_url(page_url)

    print(f"\n🔍 Scraping: {page_title}")

    page = await context.new_page()

    try:

        await page.goto(
            full_url,
            wait_until="networkidle",
            timeout=60000
        )

        await page.wait_for_timeout(3000)

        # -------------------------------------------------
        # CONTENT SELECTORS
        # -------------------------------------------------

        main_selectors = [
            ".show-content",
            ".user_content",
            ".page-content",
            "#wiki_page_show",
            "main",
            "body"
        ]

        html = None

        for selector in main_selectors:

            try:

                exists = await page.query_selector(
                    selector
                )

                if exists:

                    html = await page.inner_html(
                        selector
                    )

                    break

            except:
                pass

        # fallback
        if not html:

            html = await page.inner_html("body")

        # -------------------------------------------------
        # PARSE HTML
        # -------------------------------------------------

        soup = BeautifulSoup(
            html,
            "lxml"
        )

        # -------------------------------------------------
        # EXTRACT ATTACHMENTS
        # -------------------------------------------------

        attachments = extract_attachments(
            soup
        )

        # -------------------------------------------------
        # PRESERVE MEDIA INLINE
        # -------------------------------------------------

        soup = preserve_media_inline(
            soup
        )

        # -------------------------------------------------
        # CLEAN HTML
        # -------------------------------------------------

        soup = clean_canvas_html(
            soup
        )

        # -------------------------------------------------
        # CONVERT TO MARKDOWN
        # -------------------------------------------------

        markdown_content = md(
            str(soup),
            heading_style="ATX"
        )

        # -------------------------------------------------
        # OPTIONAL FIRECRAWL ENHANCEMENT
        # -------------------------------------------------

        firecrawl_md = try_firecrawl(
            full_url
        )

        if (
            firecrawl_md
            and len(firecrawl_md)
            > len(markdown_content)
        ):

            markdown_content = firecrawl_md

        # -------------------------------------------------
        # BUILD FINAL MARKDOWN
        # -------------------------------------------------

        final_markdown = (
            build_enriched_markdown(
                title=page_title,
                markdown_content=markdown_content,
                attachments=attachments,
                source_url=full_url
            )
        )

        # -------------------------------------------------
        # SAVE FILE
        # -------------------------------------------------

        await save_markdown(
            final_markdown,
            folder_path,
            page_title,
            item_index
        )

    except Exception as e:

        print(
            f"❌ Error scraping "
            f"{page_title}: {e}"
        )

    finally:

        await page.close()


# =========================================================
# MAIN COURSE SCRAPER
# =========================================================

async def scrape_course():

    async with async_playwright() as p:

        browser = await p.chromium.launch(
            headless=HEADLESS
        )

        # -------------------------------------------------
        # AUTH CHECK
        # -------------------------------------------------

        if not os.path.exists("auth.json"):

            print(
                "\n❌ auth.json missing."
            )

            print(
                "Run login.py first.\n"
            )

            return

        # -------------------------------------------------
        # LOAD SAVED SESSION
        # -------------------------------------------------

        context = await browser.new_context(
            storage_state="auth.json"
        )

        page = await context.new_page()

        modules_url = (
            f"{BASE_URL}/courses/"
            f"{COURSE_ID}/modules"
        )

        print("\n🚀 Opening modules page")

        await page.goto(
            modules_url,
            wait_until="networkidle",
            timeout=60000
        )

        # -------------------------------------------------
        # WAIT FOR MODULES
        # -------------------------------------------------

        await page.wait_for_selector(
            ".context_module",
            timeout=60000
        )

        modules = await page.query_selector_all(
            ".context_module"
        )

        print(
            f"\n📚 Found "
            f"{len(modules)} modules"
        )

        # -------------------------------------------------
        # LOOP MODULES
        # -------------------------------------------------

        for module_index, module in enumerate(
            modules,
            start=1
        ):

            try:

                header = await module.query_selector(
                    ".header"
                )

                raw_title = (
                    await header.inner_text()
                )

                module_title = sanitize_name(
                    raw_title.split("\n")[0]
                )

            except:

                module_title = "General"

            numbered_module_title = (
                f"{module_index:02d}_"
                f"{module_title}"
            )

            print(
                "\n====================="
            )

            print(
                f"📦 MODULE: "
                f"{numbered_module_title}"
            )

            print(
                "====================="
            )

            folder_path = os.path.join(
                DATA_DIR,
                numbered_module_title
            )

            rows = await module.query_selector_all(
                ".context_module_item"
            )

            print(
                f"Found {len(rows)} items"
            )

            # -------------------------------------------------
            # LOOP ITEMS
            # -------------------------------------------------

            for item_index, row in enumerate(
                rows,
                start=1
            ):

                try:

                    link_el = await row.query_selector(
                        "a.ig-title"
                    )

                    if not link_el:
                        continue

                    page_title = (
                        await link_el.inner_text()
                    ).strip()

                    page_url = (
                        await link_el.get_attribute(
                            "href"
                        )
                    )

                    if not page_url:
                        continue

                    # -----------------------------------------
                    # SKIP FILTERS
                    # -----------------------------------------

                    if any(
                        skip.lower()
                        in page_title.lower()
                        for skip in SKIP_LIST
                    ):

                        print(
                            f"⏩ Skipping: "
                            f"{page_title}"
                        )

                        continue

                    # skip quizzes/tools
                    if (
                        "quiz" in page_url.lower()
                        or "external_tools"
                        in page_url.lower()
                    ):

                        print(
                            f"⏩ Skipping "
                            f"tool/quiz: "
                            f"{page_title}"
                        )

                        continue

                    # -----------------------------------------
                    # SCRAPE PAGE
                    # -----------------------------------------

                    await scrape_page(
                        context=context,
                        page_title=page_title,
                        page_url=page_url,
                        folder_path=folder_path,
                        item_index=item_index
                    )

                    await asyncio.sleep(2)

                except Exception as e:

                    print(
                        f"⚠️ Row processing "
                        f"error: {e}"
                    )

        await browser.close()

        print(
            "\n✨ COURSE SCRAPING COMPLETE"
        )


# =========================================================
# ENTRY POINT
# =========================================================

if __name__ == "__main__":

    try:

        asyncio.run(
            scrape_course()
        )

    except KeyboardInterrupt:

        print("\n🛑 Scraper stopped")