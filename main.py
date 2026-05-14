import os
import asyncio
import re
from dotenv import load_dotenv
from playwright.async_api import async_playwright
from firecrawl import FirecrawlApp

# 1. Setup & Configuration
load_dotenv()
FIRECRAWL_KEY = os.getenv("FIRECRAWL_API_KEY")
BASE_URL = "https://moringa.instructure.com"

# Initialize Firecrawl
app = FirecrawlApp(api_key=FIRECRAWL_KEY)

# Pages to ignore
SKIP_LIST = [
    "Student Contract", 
    "Data Policy", 
    "Media Consent Form", 
    "Student Handbook", 
    "Student Resources",
    "Moringa School Emergency Policy and Procedure"
]

def sanitize_name(name):
    """Removes characters that are illegal in Windows file/folder names."""
    # Removes characters like : / \ * ? " < > |
    return re.sub(r'[<>:"/\\|?*]', '', name).strip()

async def save_markdown(content, folder_path, filename):
    """Saves the scraped content to a local markdown file."""
    os.makedirs(folder_path, exist_ok=True)
    clean_filename = sanitize_name(filename)
    file_path = os.path.join(folder_path, f"{clean_filename}.md")
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"✅ Saved: {file_path}")

async def scrape_course():
    async with async_playwright() as p:
        # Launch browser
        browser = await p.chromium.launch(headless=False)
        
        if not os.path.exists("auth.json"):
            print("❌ Error: auth.json missing! Please run the login script first.")
            return

        # Load existing session
        context = await browser.new_context(storage_state="auth.json")
        page = await context.new_page()

        print("🚀 Navigating to Course Modules...")
        # Note: Using your specific course ID 1391 from previous logs
        await page.goto(f"{BASE_URL}/courses/1391/modules")
        
        # Wait for the modules list to appear
        try:
            await page.wait_for_selector("#context_modules", timeout=60000)
        except Exception:
            print("❌ Timeout: Could not find modules. Check your login session or URL.")
            await browser.close()
            return

        # Find all Module containers (Weeks/Units)
        weeks = await page.query_selector_all(".context_module")
        
        for week in weeks:
            # Extract and sanitize the Week/Module title for the folder name
            raw_week_title = await week.query_selector(".header")
            week_text = await raw_week_title.inner_text() if raw_week_title else "General"
            week_title = sanitize_name(week_text.split('\n')[0])
            
            print(f"\n--- Processing: {week_title} ---")
            
            # Find all items within this module
            rows = await week.query_selector_all(".context_module_item")
            
            for row in rows:
                link_el = await row.query_selector("a.ig-title")
                if not link_el:
                    continue
                
                page_title = (await link_el.inner_text()).strip()
                page_url = await link_el.get_attribute("href")
                
                # Filter out unwanted pages
                if any(skip.lower() in page_title.lower() for skip in SKIP_LIST):
                    print(f"⏩ Skipping (Skip List): {page_title}")
                    continue

                # Filter out quizzes or external tools that don't scrape well as MD
                if "quiz" in page_url.lower() or "external_tools" in page_url.lower():
                    print(f"⏩ Skipping (Non-Content): {page_title}")
                    continue

                # 4. Extract Content
                print(f"🔍 Scraping: {page_title}...")
                
                content_page = await context.new_page()
                try:
                    await content_page.goto(f"{BASE_URL}{page_url}", wait_until="load", timeout=45000)
                    
                    # Firecrawl logic: Handle both Object and Dictionary responses
                    try:
                        result = app.scrape_url(f"{BASE_URL}{page_url}", params={'formats': ['markdown']})
                        
                        # Check if result is an object with a .markdown attribute
                        if hasattr(result, 'markdown'):
                            markdown_content = result.markdown
                        # Check if result is a dictionary
                        elif isinstance(result, dict):
                            markdown_content = result.get('markdown', "No content found in dict.")
                        else:
                            markdown_content = str(result)
                            
                    except Exception as e:
                        print(f"⚠️ Firecrawl call failed, trying backup: {e}")
                        # Final fallback: just get the text from the page via Playwright
                        markdown_content = await content_page.inner_text("body")

                    # Save to the data folder
                    folder_path = os.path.join("data", week_title)
                    await save_markdown(markdown_content, folder_path, page_title)

                except Exception as e:
                    print(f"⚠️ Error processing {page_title}: {e}")
                finally:
                    await content_page.close()
                
                # Brief pause to avoid rate limiting
                await asyncio.sleep(2)

        await browser.close()
        print("\n✨ Scraping Complete!")

if __name__ == "__main__":
    try:
        asyncio.run(scrape_course())
    except KeyboardInterrupt:
        print("\n🛑 Scraper stopped by user.")