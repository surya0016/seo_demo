import serpapi
from urllib.parse import urlparse

SERPAPI_API_KEY = "8049b857b6eed9d7a3eb276779cffd9b689f36099a51cd5947a44b32a67dbd98"

client = serpapi.Client(api_key=SERPAPI_API_KEY)


def get_top_5_sites(query):
    search = client.search({
        "q": query,
        "location": "India",
        "hl": "en",
        "gl": "in",
        "num": 20,
        "api_key": SERPAPI_API_KEY
    })

    results = search.as_dict()

    if 'organic_results' not in results:
        print("No results found or error in API response.")
        return []

    filtered_links = []
    seen_domains = set()

    for result in results['organic_results']:
        link = result.get('link', '')

        # Validation checking
        if not link.startswith("http"):
            continue
        if any(sub in link for sub in ["wikipedia.org", "/search?", "google.com", "youtube.com"]):
            continue

        # Remove duplicate url
        domain = urlparse(link).netloc
        if domain in seen_domains:
            continue
        seen_domains.add(domain)

        filtered_links.append(link)

        if len(filtered_links) == 5:
            break

    return filtered_links


def save_links_to_file(links):
    filename = input("Enter file name: ")
    with open(filename, 'w') as f:
        for link in links:
            f.write(link + '\n')
    print(f"\nLinks saved to {filename}")


if __name__ == "__main__":
    keyword = input("Enter a keyword to search: ")
    top_links = get_top_5_sites(keyword)

    if top_links:
        print("\nTop 5 Organic and Relevant Links (No Duplicates):\n")
        for i, link in enumerate(top_links, 1):
            print(f"{i}. {link}")

        # Save links to file
        save_links_to_file(top_links)
    else:
        print("No relevant sites found.")