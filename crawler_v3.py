# Requirements: playwright, beautifulsoup4, requests, lxml
# Install: pip install playwright beautifulsoup4 lxml requests && playwright install

import asyncio
from urllib.parse import urlparse, urljoin # Import urljoin for handling relative URLs
from playwright.async_api import async_playwright
from bs4 import BeautifulSoup
import json
import re

# Set to store visited URLs to prevent redundant crawling and infinite loops on internal links
# This is crucial for a basic crawler to avoid re-processing the same pages.
visited_urls = set()
# List to store all extracted SEO data from multiple crawled pages
all_seo_data = []

async def extract_seo_data(url, target_keyword=""):
    # Add the current URL to the set of visited URLs
    visited_urls.add(url)
    print(f"Crawling: {url}") # Print which URL is currently being crawled

    async with async_playwright() as p:
        # Launch a Chromium browser in headless mode (no UI)
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        try:
            # Navigate to the URL with a timeout of 60 seconds
            await page.goto(url, timeout=60000)
            # Get the full HTML content of the page
            html = await page.content()
        except Exception as e:
            # Handle potential errors during page navigation (e.g., page not found, timeout)
            print(f"Error navigating to {url}: {e}")
            await browser.close()
            return None # Return None if there's an error
        finally:
            await browser.close() # Ensure the browser is closed even if an error occurs

        # Parse the URL to extract components like domain, path
        parsed_url = urlparse(url)
        # Create a BeautifulSoup object to parse the HTML using lxml parser for speed
        soup = BeautifulSoup(html, 'lxml')

        # --- Meta tags extraction ---
        # Get the page title, stripping whitespace. If no title, default to empty string.
        title = soup.title.string.strip() if soup.title else ''
        meta_desc = '' # Initialize meta description
        meta_keywords = '' # Initialize meta keywords
        canonical_url = '' # Initialize canonical URL

        # Find all <meta> tags
        for tag in soup.find_all('meta'):
            name = tag.get('name', '').lower() # Get the 'name' attribute, convert to lowercase
            if name == 'description':
                meta_desc = tag.get('content', '') # Extract content for description
            elif name == 'keywords':
                meta_keywords = tag.get('content', '') # Extract content for keywords

        # Find the canonical link tag and extract its href
        canonical_tag = soup.find("link", rel="canonical")
        if canonical_tag:
            canonical_url = canonical_tag.get("href", "")

        # --- Headings extraction ---
        # Extract text content from all <h1>, <h2>, and <h3> tags
        headings = {
            'h1': [h.get_text(strip=True) for h in soup.find_all('h1')],
            'h2': [h.get_text(strip=True) for h in soup.find_all('h2')],
            'h3': [h.get_text(strip=True) for h in soup.find_all('h3')],
        }

        # --- Main content extraction and keyword density calculation ---
        # Find common content blocks (article, main, p)
        content_blocks = soup.find_all(['article', 'main', 'p'])
        # Join the text from these blocks into a single string
        all_text = ' '.join([block.get_text(strip=True) for block in content_blocks])
        # Count words using regex to find word characters
        word_count = len(re.findall(r'\w+', all_text))
        keyword_density = 0
        # If a target keyword is provided, calculate its density
        if target_keyword:
            # Count keyword occurrences (case-insensitive) and divide by total words
            keyword_density = all_text.lower().count(target_keyword.lower()) / max(word_count, 1)

        # --- URL structure analysis ---
        path = parsed_url.path # Get the path component of the URL
        # Extract the slug (last part of the path)
        slug = path.strip("/").split("/")[-1]

        # --- Image SEO (alt attributes) ---
        images = soup.find_all('img') # Find all <img> tags
        # Create a list of dictionaries with 'src' and 'alt' attributes for images that have a 'src'
        image_data = [{'src': img.get('src'), 'alt': img.get('alt')} for img in images if img.get('src')]

        # --- Link analysis (internal and external) ---
        internal_links = []
        external_links = []
        # Iterate through all <a> tags with an 'href' attribute
        for a in soup.find_all('a', href=True):
            href = a['href']
            # Resolve relative URLs to absolute URLs
            absolute_href = urljoin(url, href).split('#')[0] # Remove fragment identifiers

            # Check if the link has already been visited or is a common non-crawlable link
            if absolute_href in visited_urls or \
               absolute_href.startswith("mailto:") or \
               absolute_href.startswith("tel:"):
                continue

            # Check if the link belongs to the same domain (internal) or different (external)
            if parsed_url.netloc in absolute_href:
                internal_links.append(absolute_href)
            else:
                external_links.append(absolute_href)

        # --- Schema (Structured Data) extraction ---
        schemas = []
        # Find all <script> tags of type "application/ld+json" (JSON-LD schema)
        for script in soup.find_all("script", {"type": "application/ld+json"}):
            try:
                # Attempt to parse the script content as JSON
                schemas.append(json.loads(script.string.strip()))
            except:
                continue # Skip if JSON parsing fails

        # Compile all extracted SEO data into a dictionary
        seo_data = {
            'url': url,
            'canonical_url': canonical_url,
            'title': title,
            'meta_description': meta_desc,
            'meta_keywords': meta_keywords,
            'headings': headings,
            'content_summary': all_text[:500],  # Show first 500 chars of main content
            'word_count': word_count,
            'keyword_density': round(keyword_density, 4),
            'slug': slug,
            'path': path,
            # 'images': image_data,
            'internal_links': internal_links[:20], # Limit to first 20 internal links for brevity
            'external_links': external_links[:20], # Limit to first 20 external links for brevity
            'schemas': schemas[:2] # Sample first 2 schema objects
        }

        return seo_data

# Asynchronous main function to orchestrate the crawling process
async def main():
    # Define a list of URLs to crawl. You can add as many as you need here.
    # For a full website crawl, you would typically start with a base URL
    # and recursively follow internal links up to a certain depth.
    # This example demonstrates processing a predefined list of URLs.
    urls_to_crawl = [
        'https://thepeppystore.in/collections/keychains?srsltid=AfmBOoqwLdr4Fu6BLq5zEyFczP2qRd3KC74v9b_ATpIYWTJ28Fp_hVQD',
        'https://store.twentyonepilots.com/products/blurryface-anniversary-keychain?srsltid=AfmBOoo7gp4ftGeP-BAfbul__Rbo47y1Mp6raxN5Av9MwA5MXeeGO3OC',
    ]

    target_keyword = "ITIN application assistance"  # Optional global keyword for density analysis

    # Use a set to keep track of URLs that are already scheduled for crawling
    # to avoid adding the same URL multiple times if found via different paths.
    urls_to_process = set(urls_to_crawl)

    # Simple queue for links found to be crawled. For a more robust crawler,
    # you might use a proper queue data structure and handle crawl depth.
    crawling_queue = list(urls_to_process)

    while crawling_queue:
        current_url = crawling_queue.pop(0) # Get the next URL from the queue

        if current_url in visited_urls:
            continue # Skip if already visited

        # Extract SEO data for the current URL
        seo_data = await extract_seo_data(current_url, target_keyword)

        if seo_data:
            all_seo_data.append(seo_data) # Add extracted data to our global list

            # You can uncomment the following block to enable basic recursive crawling
            # of internal links found on the current page up to a certain depth.
            # Be cautious with this, as it can crawl many pages quickly!
            # For a real crawler, implement depth limits and domain restrictions.

            # for link in seo_data['internal_links']:
            #     # Ensure the link is absolute and belongs to the same main domain as the starting URL
            #     # and hasn't been visited or scheduled yet.
            #     if urlparse(link).netloc == parsed_url.netloc and link not in visited_urls and link not in urls_to_process:
            #         urls_to_process.add(link)
            #         crawling_queue.append(link)


    # After crawling all specified URLs, print all the collected data
    print("\n--- All Collected SEO Data ---")
    print(json.dumps(all_seo_data, indent=2))

    # Optional: Save the data to a JSON file
    with open("seo_crawl_results.json", "w", encoding="utf-8") as f:
        json.dump(all_seo_data, f, indent=2, ensure_ascii=False)
    print("\nSEO data saved to seo_crawl_results.json")


# This block ensures that the main asynchronous function is run when the script is executed.
if __name__ == '__main__':
    asyncio.run(main())