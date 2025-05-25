import asyncio
from urllib.parse import urlparse, urljoin # Import urljoin for handling relative URLs
from playwright.async_api import async_playwright
from bs4 import BeautifulSoup
import json
import re

visited_urls = set()

all_seo_data = []

async def extract_seo_data(url, target_keyword=""):
    visited_urls.add(url)
    print(f"Crawling: {url}")

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        try:
            await page.goto(url, timeout=60000)
            html = await page.content()
        except Exception as e:
            print(f"Error navigating to {url}: {e}")
            await browser.close()
            return None
        finally:
            await browser.close()


        parsed_url = urlparse(url)

        soup = BeautifulSoup(html, 'lxml')

        # --- Meta tags extraction ---
        title = soup.title.string.strip() if soup.title else ''
        meta_desc = ''
        meta_keywords = ''
        canonical_url = ''

        for tag in soup.find_all('meta'):
            name = tag.get('name', '').lower()
            if name == 'description':
                meta_desc = tag.get('content', '')
            elif name == 'keywords':
                meta_keywords = tag.get('content', '')

        canonical_tag = soup.find("link", rel="canonical")
        if canonical_tag:
            canonical_url = canonical_tag.get("href", "")

        # --- Headings extraction ---
        headings = {
            'h1': [h.get_text(strip=True) for h in soup.find_all('h1')],
            'h2': [h.get_text(strip=True) for h in soup.find_all('h2')],
            'h3': [h.get_text(strip=True) for h in soup.find_all('h3')],
        }

        # --- Main content extraction and keyword density calculation ---
        content_blocks = soup.find_all(['article', 'main', 'p'])
        all_text = ' '.join([block.get_text(strip=True) for block in content_blocks])
        word_count = len(re.findall(r'\w+', all_text))
        keyword_density = 0
        if target_keyword:
            keyword_density = all_text.lower().count(target_keyword.lower()) / max(word_count, 1)

        # --- URL structure analysis ---
        path = parsed_url.path
        slug = path.strip("/").split("/")[-1]

        # --- Image SEO (alt attributes) ---
        images = soup.find_all('img')
        image_data = [{'src': img.get('src'), 'alt': img.get('alt')} for img in images if img.get('src')]

        # --- Link analysis (internal and external) ---
        internal_links = []
        external_links = []
        for a in soup.find_all('a', href=True):
            href = a['href']

            absolute_href = urljoin(url, href).split('#')[0]

            if absolute_href in visited_urls or \
               absolute_href.startswith("mailto:") or \
               absolute_href.startswith("tel:"):
                continue

            if parsed_url.netloc in absolute_href:
                internal_links.append(absolute_href)
            else:
                external_links.append(absolute_href)

        # --- Schema (Structured Data) extraction ---
        schemas = []

        for script in soup.find_all("script", {"type": "application/ld+json"}):
            try:
                schemas.append(json.loads(script.string.strip()))
            except:
                continue

        # Compile all extracted SEO data into a dictionary
        seo_data = {
            'url': url,
            'canonical_url': canonical_url,
            'title': title,
            'meta_description': meta_desc,
            'meta_keywords': meta_keywords,
            'headings': headings,
            'content_summary': all_text[:500],
            'word_count': word_count,
            'keyword_density': round(keyword_density, 4),
            'slug': slug,
            'path': path,
            # 'images': image_data,
            'internal_links': internal_links[:20],
            'external_links': external_links[:20],
            'schemas': schemas[:2]
        }

        return seo_data

# Asynchronous main function to orchestrate the crawling process
async def main():
    link1 = input("Enter the first link: ")
    link2 = input("Enter the second link: ")
    link3 = input("Enter the third link: ")
    link4 = input("Enter client link: ")

    urls_to_crawl = [link1, link2, link3, link4]
    target_keyword = "ITIN application assistance"

    urls_to_process = set(urls_to_crawl)
    crawling_queue = list(urls_to_process)

    while crawling_queue:
        current_url = crawling_queue.pop(0)

        if current_url in visited_urls:
            continue

        seo_data = await extract_seo_data(current_url, target_keyword)

        if seo_data:
            all_seo_data.append(seo_data)

    print("\n--- All Collected SEO Data ---")
    print(json.dumps(all_seo_data, indent=2))

    with open("seo_crawl_results.json", "w", encoding="utf-8") as f:
        json.dump(all_seo_data, f, indent=2, ensure_ascii=False)
    print("\nSEO data saved to seo_crawl_results.json")

if __name__ == '__main__':
    asyncio.run(main())


# https://www.amazon.in/Keyrings-Keychains/b?ie=UTF8&node=2917480031
# https://thepeppystore.in/collections/keychains?srsltid=AfmBOoqwLdr4Fu6BLq5zEyFczP2qRd3KC74v9b_ATpIYWTJ28Fp_hVQD
# https://www.giftoo.in/collections/keychians?srsltid=AfmBOopt0j6CVSYmTInDZ9noSXlkG5EiN3oYzU0ZTatZuJV_oPB75EM-

# https://www.popmart.com/us/pop-now/set/201?srsltid=AfmBOorXlPlrce3vV0oihRyf0Y6PWhDQ_-ZwBEPyQ5n89t6vBuiZ6NqJ