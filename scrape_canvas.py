import os
import re
import asyncio
from datetime import datetime

from playwright.async_api import async_playwright
from bs4 import BeautifulSoup
from markdownify import markdownify as md

# =========================================================
# CONFIGURATION
# =========================================================

BASE_URL = "https://moringa.instructure.com"
COURSE_ID = "1426"

HEADLESS = False

DATA_DIR = "data/Module3"



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

    return re.sub(
        r'[<>:"/\\|?*]',
        '',
        name
    ).strip()


def ensure_absolute_url(url):

    if not url:
        return url

    if url.startswith("http"):
        return url

    return f"{BASE_URL}{url}"


def file_exists(folder_path, filename, index):

    clean_filename = sanitize_name(
        filename
    )

    numbered_filename = (
        f"{index:02d}_{clean_filename}.md"
    )

    filepath = os.path.join(
        folder_path,
        numbered_filename
    )

    return os.path.exists(filepath)


async def save_markdown(
    content,
    folder_path,
    filename,
    order_index
):

    os.makedirs(
        folder_path,
        exist_ok=True
    )

    clean_filename = sanitize_name(
        filename
    )

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
    # IFRAMES
    # -----------------------------------------------------

    for iframe in soup.find_all("iframe"):

        src = iframe.get("src")

        if not src:
            continue

        src = ensure_absolute_url(src)

        iframe_text = (
            f"\n\n[VIDEO LINK]({src})\n\n"
        )

        iframe.replace_with(
            iframe_text
        )

    # -----------------------------------------------------
    # HTML5 VIDEOS
    # -----------------------------------------------------

    for video in soup.find_all("video"):

        src = video.get("src")

        if not src:

            source = video.find(
                "source"
            )

            if source:
                src = source.get("src")

        if not src:
            continue

        src = ensure_absolute_url(src)

        video_text = (
            f"\n\n[VIDEO LINK]({src})\n\n"
        )

        video.replace_with(
            video_text
        )

    return soup


# =========================================================
# ATTACHMENTS
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

    for a in soup.find_all(
        "a",
        href=True
    ):

        href = a["href"]

        if any(
            ext in href.lower()
            for ext in allowed_extensions
        ):

            attachments.append({
                "name": a.get_text(
                    strip=True
                ),
                "url": ensure_absolute_url(
                    href
                )
            })

    return attachments


# =========================================================
# CLEAN HTML
# =========================================================

def clean_canvas_html(soup):

    for tag in soup.find_all([
        "script",
        "style",
        "noscript"
    ]):
        tag.decompose()

    selectors_to_remove = [
        ".header-bar",
        ".navigation",
        ".breadcrumbs",
        ".module-sequence-footer",
        ".course-title",
        ".ic-app-nav-toggle-and-crumbs"
    ]

    for selector in selectors_to_remove:

        for el in soup.select(
            selector
        ):
            el.decompose()

    return soup


# =========================================================
# BUILD MARKDOWN
# =========================================================

def build_enriched_markdown(
    title,
    markdown_content,
    attachments,
    source_url
):

    final_md = f"# {title}\n\n"

    final_md += (
        markdown_content.strip()
    )

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
        f"Original URL: "
        f"{source_url}\n\n"
    )

    final_md += (
        f"Scraped At: "
        f"{datetime.now().isoformat()}\n"
    )

    return final_md





# =========================================================
# SCRAPE PAGE
# =========================================================

async def scrape_page(
    context,
    page_title,
    page_url,
    folder_path,
    item_index
):

    # -----------------------------------------------------
    # RESUME SUPPORT
    # -----------------------------------------------------

    if file_exists(
        folder_path,
        page_title,
        item_index
    ):

        print(
            f"⏩ Already exists: "
            f"{page_title}"
        )

        return

    full_url = ensure_absolute_url(
        page_url
    )

    print(
        f"\n🔍 Scraping: "
        f"{page_title}"
    )

    page = await context.new_page()

    try:

        await page.goto(
            full_url,
            wait_until="networkidle",
            timeout=60000
        )

        # Wait for the main content selector to appear
        # instead of a fixed sleep
        for selector in [
            ".show-content",
            ".user_content",
            ".page-content",
            "#wiki_page_show",
            "main"
        ]:
            try:
                await page.wait_for_selector(
                    selector,
                    timeout=5000
                )
                break
            except:
                pass

        print(
            f"✅ Loaded: "
            f"{page_title}"
        )

        # -------------------------------------------------
        # MAIN CONTENT SELECTORS
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

            html = await page.inner_html(
                "body"
            )

        # -------------------------------------------------
        # PARSE HTML
        # -------------------------------------------------

        soup = BeautifulSoup(
            html,
            "lxml"
        )

        # -------------------------------------------------
        # ATTACHMENTS
        # -------------------------------------------------

        attachments = (
            extract_attachments(
                soup
            )
        )

        # -------------------------------------------------
        # INLINE MEDIA
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
        # HTML -> MARKDOWN
        # -------------------------------------------------

        markdown_content = md(
            str(soup),
            heading_style="ATX"
        )


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
        # SAVE FILE — folders created here, not before
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
# MAIN SCRAPER
# =========================================================

async def scrape_course():

    async with async_playwright() as p:

        browser = await p.chromium.launch(
            headless=HEADLESS
        )

        # -------------------------------------------------
        # AUTH CHECK
        # -------------------------------------------------

        if not os.path.exists(
            "auth.json"
        ):

            print(
                "\n❌ auth.json missing."
            )

            print(
                "Run login.py first.\n"
            )

            return

        # -------------------------------------------------
        # LOAD SESSION
        # -------------------------------------------------

        context = await browser.new_context(
            storage_state="auth.json"
        )

        page = await context.new_page()

        modules_url = (
            f"{BASE_URL}/courses/"
            f"{COURSE_ID}/modules"
        )

        print(
            "\n🚀 Opening modules page"
        )

        print(modules_url)

        # networkidle waits for Canvas JS to finish
        # rendering all modules before we touch the DOM
        await page.goto(
            modules_url,
            wait_until="networkidle",
            timeout=90000
        )

        print("✅ Modules page loaded")

        print(
            f"📄 Page Title: "
            f"{await page.title()}"
        )

        # -------------------------------------------------
        # CHECK IF LOGIN EXPIRED
        # -------------------------------------------------

        current_url = page.url

        if "login" in current_url.lower():

            print(
                "\n❌ Session expired."
            )

            print(
                "Recreate auth.json"
            )

            return

        # -------------------------------------------------
        # WAIT FOR AT LEAST ONE MODULE IN THE DOM
        # -------------------------------------------------

        print(
            "⏳ Waiting for modules to render..."
        )

        await page.wait_for_selector(
            ".context_module",
            timeout=60000
        )

        print(
            "✅ Modules detected"
        )

        # -------------------------------------------------
        # EXPAND ALL COLLAPSED MODULES AT ONCE
        # Single JS call — avoids slow sequential awaits
        # -------------------------------------------------

        await page.evaluate(
            """
            document
                .querySelectorAll('.expand_module_link')
                .forEach(btn => btn.click());
            """
        )

        # Wait for expansion network requests to settle
        await page.wait_for_load_state(
            "networkidle"
        )

        modules = await page.query_selector_all(
            ".context_module"
        )

        print(
            f"\n📚 Found "
            f"{len(modules)} modules"
        )

        # =================================================
        # LOOP MODULES
        # =================================================

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

            # Module folder is NOT created here.
            # It will be created lazily inside
            # save_markdown only when a file is
            # actually written.

            module_folder = os.path.join(
                DATA_DIR,
                numbered_module_title
            )

            rows = await module.query_selector_all(
                ".context_module_item"
            )

            print(
                f"Found {len(rows)} items"
            )

            # =================================================
            # SECTION TRACKING
            # =================================================

            current_section = None

            section_index = 1

            item_index = 1

            # =================================================
            # LOOP ROWS
            # =================================================

            for row in rows:

                try:

                    # -----------------------------------------
                    # ROW CLASS
                    # -----------------------------------------

                    row_class = (
                        await row.get_attribute(
                            "class"
                        )
                    ) or ""

                    # =================================================
                    # SECTION HEADER DETECTION
                    # =================================================

                    if (
                        "context_module_sub_header"
                        in row_class
                    ):

                        section_title_el = await row.query_selector(
                            "span.title"
                        )

                        if section_title_el:

                            section_title = (
                                await section_title_el.inner_text()
                            ).strip()

                            if section_title:

                                current_section = (
                                    f"{section_index:02d}_"
                                    f"{sanitize_name(section_title)}"
                                )

                                section_index += 1

                                print(
                                    f"\n📁 SECTION: "
                                    f"{current_section}"
                                )

                        continue

                    # =================================================
                    # NORMAL CONTENT ITEM
                    # =================================================

                    link_el = await row.query_selector(
                        "a.ig-title"
                    )

                    if not link_el:
                        continue

                    # -----------------------------------------
                    # PAGE TITLE
                    # -----------------------------------------

                    page_title = (
                        await link_el.inner_text()
                    ).strip()

                    # -----------------------------------------
                    # PAGE URL
                    # -----------------------------------------

                    page_url = (
                        await link_el.get_attribute(
                            "href"
                        )
                    )

                    if not page_url:
                        continue

                    # =================================================
                    # SKIP LIST
                    # =================================================

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

                    # =================================================
                    # SKIP QUIZZES / TOOLS
                    # =================================================

                    if (
                        "quiz" in page_url.lower()
                        or "external_tools"
                        in page_url.lower()
                    ):

                        print(
                            f"⏩ Skipping tool/quiz: "
                            f"{page_title}"
                        )

                        continue

                    # =================================================
                    # RESOLVE TARGET FOLDER
                    # Items before the first sub-header go directly
                    # into the module folder (no subfolder).
                    # =================================================

                    if current_section:
                        section_folder = os.path.join(
                            module_folder,
                            current_section
                        )
                    else:
                        # No sub-header yet — save at module root
                        section_folder = module_folder

                    # =================================================
                    # SCRAPE PAGE
                    # =================================================

                    await scrape_page(
                        context=context,
                        page_title=page_title,
                        page_url=page_url,
                        folder_path=section_folder,
                        item_index=item_index
                    )

                    item_index += 1

                    await asyncio.sleep(0.5)

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

        print(
            "\n🛑 Scraper stopped"
        )