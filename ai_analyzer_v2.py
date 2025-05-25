from google import genai



def generate_and_save_content():
    prompt = """
    You are an Advanced SEO Analyst and Strategist, powered by Gemini. Your mission is to help users optimize their webpages by performing a deep comparative on-page SEO analysis, and providing highly specific, actionable recommendations to outperform them.
    <title> Tag Content
    Heading Tags (<h1> - <h6>) Content & Hierarchical Structure
    Main Body Content (Processed into analyzable text, e.g., Markdown, preserving structure)
    Internal Links (Anchor Text & Target URL)
    Schema Markup / Structured Data (Type and key properties, e.g., JSON-LD)
    Meta Description Content
    Medium Priority (Supporting Context):
    Image alt Attributes
    Full URL Structure
    External Links (Anchor Text & Target URL)
    Lower Priority (Emphasis Indicators):
    Content within <b> / <strong> tags
    Analyze & Compare:
    Process the given structured data.
    DATA:{
    Competitors Page Data:
    {
        "url": "https://thepeppystore.in/collections/keychains?srsltid=AfmBOoqwLdr4Fu6BLq5zEyFczP2qRd3KC74v9b_ATpIYWTJ28Fp_hVQD",
        "canonical_url": "https://thepeppystore.in/collections/keychains",
        "title": "Shop Quirky Keychains in India- The Peppy Store",
        "meta_description": "Shop all the quirky keychains now available at THE PEPPY STORE. Choose from wide Variety of keychains like Harry Potter, Friends etc. from one place. Shop Now! Shipping Pan India, Cash on Delivery Available and Online Payments Available!",
        "meta_keywords": "",
        "headings": {
          "h1": [],
          "h2": [],
          "h3": []
        },
        "content_summary": "Cart Your cart is empty FilterSort bySort byFeaturedBest sellingAlphabetically, A-ZAlphabetically, Z-APrice, low to highPrice, high to lowDate, old to newDate, new to old256 productsFiltersAvailabilityIn stock onlyPrice\u20b9INRto\u20b9INRView resultsView resultsAdd To CartCute Dog Keychain With BagcharmSale priceRs. 199.00 INRChoose optionsMini Retro  Recorder KeychainSale priceRs. 299.00 INRColorPinkBlackPurpleWhite(5.0)Add To CartGirl Pvc KeychainSale priceRs. 220.00 INRChoose optionsTransformers Bumbl",
        "word_count": 726,
        "keyword_density": 0.0,
        "slug": "keychains",
        "path": "/collections/keychains",
        "internal_links": [
          "https://thepeppystore.in/",
          "https://thepeppystore.in/collections/official-hot-wheels-mattel-toys",
          "https://thepeppystore.in/collections/hotwheels-2025-c-and-d-case",
          "https://thepeppystore.in/collections/imported-2025-e-and-f-case",
          "https://thepeppystore.in/collections/j-and-k-case-2025",
          "https://thepeppystore.in/collections/fast-and-furious",
          "https://thepeppystore.in/collections/pop-culture-hotwheels-imported",
          "https://thepeppystore.in/collections/japan-historics",
          "https://thepeppystore.in/collections/imported-terra-treck",
          "https://thepeppystore.in/collections/team-transport-hotwheels",
          "https://thepeppystore.in/collections/transformers-hotwheels",
          "https://thepeppystore.in/collections/ultra-hots-hotwheels",
          "https://thepeppystore.in/collections/hotwheel-trucks",
          "https://thepeppystore.in/collections/imported-hotwheels-card-damaged-car-in-mint-condition",
          "https://thepeppystore.in/collections/imported-hotwheels-car-culture",
          "https://thepeppystore.in/collections/bburago-official",
          "https://thepeppystore.in/collections/scale-1-64",
          "https://thepeppystore.in/collections/bburago-scale-1-43",
          "https://thepeppystore.in/collections/bburago-scale-1-24",
          "https://thepeppystore.in/collections/bburago-scale-1-18"
        ],
        "external_links": [
          "https://reelup.io/pages/privacy-policy",
          "https://www.shopify.com?utm_campaign=poweredby&utm_medium=shopify&utm_source=onlinestore"
        ],
        "schemas": [
          {
            "@context": "https://schema.org",
            "@type": "BreadcrumbList",
            "itemListElement": [
              {
                "@type": "ListItem",
                "position": 1,
                "name": "Home",
                "item": "https://thepeppystore.in"
              },
              {
                "@type": "ListItem",
                "position": 2,
                "name": "Keychains",
                "item": "https://thepeppystore.in/collections/keychains"
              }
            ]
          }
        ]
      }
    My websites page data:
    {
        "url": "https://store.twentyonepilots.com/products/blurryface-anniversary-keychain?srsltid=AfmBOoo7gp4ftGeP-BAfbul__Rbo47y1Mp6raxN5Av9MwA5MXeeGO3OC",
        "canonical_url": "https://store.twentyonepilots.com/products/blurryface-anniversary-keychain",
        "title": "BLURRYFACE ANNIVERSARY KEYCHAIN\n \u2013 Twenty One Pilots",
        "meta_description": "Preorder expected to ship the week of 06/27/25 THE TWENTY ONE PILOTS \u2018BLURRYFACE ANNIVERSARY KEYCHAIN\u2019 1.38\u201d DIAMETER ROUND ENAMEL WITH BLACK METAL.\u00a0",
        "meta_keywords": "",
        "headings": {
          "h1": [
            "BLURRYFACE ANNIVERSARY KEYCHAIN"
          ],
          "h2": [
            "Item added to your cart",
            "Pre-Order Releases on:\n                  \n                  June 2025",
            "YOU MIGHT ALSO LIKE",
            "",
            "Subscribe to our emails",
            "SHOP BY CATEGORY",
            "PRODUCTS",
            "CUSTOMER SUPPORT",
            "Cookies Settings"
          ],
          "h3": [
            "BLURRYFACE ANNIVERSARY HOODIE",
            "BLURRYFACE ANNIVERSARY DOUBT HAT",
            "BLURRYFACE ANNIVERSARY LONGSLEEVE",
            "Blurryface (Silver Vinyl)",
            "BLURRYFACE ANNIVERSARY HOODIE",
            "BLURRYFACE ANNIVERSARY DOUBT HAT",
            "BLURRYFACE ANNIVERSARY LONGSLEEVE",
            "Blurryface (Silver Vinyl)",
            "BLURRYFACE ANNIVERSARY HOODIE",
            "BLURRYFACE ANNIVERSARY DOUBT HAT",
            "BLURRYFACE ANNIVERSARY LONGSLEEVE",
            "Blurryface (Silver Vinyl)",
            "VESSEL",
            "BLURRYFACE",
            "TRENCH",
            "SCALED AND ICY",
            "Manage Consent Preferences",
            "Cookie List"
          ]
        },
        "content_summary": "Skip to product informationOpen media 1 in gallery view1/of1Twenty One PilotsBLURRYFACE ANNIVERSARY KEYCHAINRegular price$25.00 USDRegular priceSale price$25.00 USDUnit price/perSaleSold OutPre-Order Releases on:\n                  \n                  June 2025Product variantsDefault Title\n\n                        - $25.00QuantityDecrease quantity for BLURRYFACE ANNIVERSARY KEYCHAINIncrease quantity for BLURRYFACE ANNIVERSARY KEYCHAINPre-Order NowPreorder expected to ship the week of 06/27/25THE T",
        "word_count": 560,
        "keyword_density": 0.0,
        "slug": "blurryface-anniversary-keychain",
        "path": "/products/blurryface-anniversary-keychain",
        "internal_links": [
          "https://store.twentyonepilots.com/collections/tees",
          "https://store.twentyonepilots.com/collections/hoodies",
          "https://store.twentyonepilots.com/collections/outerwear",
          "https://store.twentyonepilots.com/collections/music",
          "https://store.twentyonepilots.com/collections/accessories",
          "https://store.twentyonepilots.com/",
          "https://store.twentyonepilots.com/collections/tees",
          "https://store.twentyonepilots.com/collections/hoodies",
          "https://store.twentyonepilots.com/collections/outerwear",
          "https://store.twentyonepilots.com/collections/music",
          "https://store.twentyonepilots.com/collections/accessories",
          "https://store.twentyonepilots.com/cart",
          "https://store.twentyonepilots.com/cart",
          "https://store.twentyonepilots.com/products/blurryface-anniversary-hoodie?pr_prod_strat=jac&pr_rec_id=e9aa92038&pr_rec_pid=9979286552895&pr_ref_pid=9979286225215&pr_seq=uniform",
          "https://store.twentyonepilots.com/products/blurryface-anniversary-doubt-hat?pr_prod_strat=e5_desc&pr_rec_id=e9aa92038&pr_rec_pid=9979285406015&pr_ref_pid=9979286225215&pr_seq=uniform",
          "https://store.twentyonepilots.com/products/blurryface-anniversary-longsleeve?pr_prod_strat=jac&pr_rec_id=e9aa92038&pr_rec_pid=9980188426559&pr_ref_pid=9979286225215&pr_seq=uniform",
          "https://store.twentyonepilots.com/products/blurryface-silver-vinyl?pr_prod_strat=e5_desc&pr_rec_id=e9aa92038&pr_rec_pid=8249785712959&pr_ref_pid=9979286225215&pr_seq=uniform",
          "https://store.twentyonepilots.com/products/blurryface-anniversary-hoodie?pr_prod_strat=jac&pr_rec_id=e9aa92038&pr_rec_pid=9979286552895&pr_ref_pid=9979286225215&pr_seq=uniform",
          "https://store.twentyonepilots.com/products/blurryface-anniversary-doubt-hat?pr_prod_strat=e5_desc&pr_rec_id=e9aa92038&pr_rec_pid=9979285406015&pr_ref_pid=9979286225215&pr_seq=uniform",
          "https://store.twentyonepilots.com/products/blurryface-anniversary-longsleeve?pr_prod_strat=jac&pr_rec_id=e9aa92038&pr_rec_pid=9980188426559&pr_ref_pid=9979286225215&pr_seq=uniform"
        ],
        "external_links": [
          "https://twentyonepilots.com/",
          "https://twentyonepilots.com/",
          "https://twentyonepilots.warnerartists.net/gb/",
          "https://twentyonepilots.warnerartists.net/eu/",
          "https://www.twentyonepilotsstore.fr/",
          "https://twentyonepilots.warnerartists.net/es/",
          "https://twentyonepilots.warnerartists.net/de/",
          "https://store.warnermusic.com.au/collections/twenty-one-pilots",
          "https://store.warnermusic.ca/collections/twenty-one-pilots",
          "https://twentyonepilots.warnerartists.net/it/",
          "https://twitter.com/twentyonepilots",
          "https://www.facebook.com/twentyonepilots",
          "https://www.instagram.com/twentyonepilots/",
          "https://www.youtube.com/user/twentyonepilots",
          "https://open.spotify.com/artist/3YQKmKGau1PzlVlkL1iodx",
          "https://music.apple.com/us/artist/twenty-one-pilots/349736311",
          "https://www.tiktok.com/@twentyonepilots",
          "https://twentyonepilots.warnerartists.net/gb/",
          "https://twentyonepilots.warnerartists.net/eu/",
          "https://www.twentyonepilotsstore.fr/"
        ],
        "schemas": [
          {
            "@context": "http://schema.org",
            "@type": "Organization",
            "name": "Twenty One Pilots",
            "logo": "https://store.twentyonepilots.com/cdn/shop/files/Logo_Desktop_2x_254dfe82-ea71-45b9-b3f3-fc913b25c25a_557x.png?v=1709010877",
            "sameAs": [
              "https://twitter.com/twentyonepilots",
              "https://www.facebook.com/twentyonepilots",
              "",
              "https://www.instagram.com/twentyonepilots/",
              "",
              "",
              "https://www.youtube.com/user/twentyonepilots",
              "",
              "https://www.tiktok.com/@twentyonepilots",
              "https://open.spotify.com/artist/3YQKmKGau1PzlVlkL1iodx",
              "",
              "https://music.apple.com/us/artist/twenty-one-pilots/349736311",
              "",
              "",
              ""
            ],
            "url": "https://store.twentyonepilots.com"
          },
          {
            "@context": "http://schema.org/",
            "@type": "Product",
            "name": "BLURRYFACE ANNIVERSARY KEYCHAIN",
            "url": "https://store.twentyonepilots.com/products/blurryface-anniversary-keychain",
            "description": "\nPreorder expected to ship the week of 06/27/25\nTHE TWENTY ONE PILOTS \u2018BLURRYFACE ANNIVERSARY KEYCHAIN\u2019 1.38\u201d DIAMETER ROUND ENAMEL WITH BLACK METAL.\u00a0",
            "sku": "5021732683144",
            "brand": {
              "@type": "Thing",
              "name": "Twenty One Pilots"
            },
            "offers": [
              {
                "@type": "Offer",
                "sku": "5021732683144",
                "availability": "http://schema.org/InStock",
                "price": 25.0,
                "priceCurrency": "USD",
                "url": "https://store.twentyonepilots.com/products/blurryface-anniversary-keychain?variant=50912736346431"
              }
            ]
          }
        ]
      }
    Perform a thorough comparative analysis of the user's page against the identified and crawled competitor pages, focusing on the extracted elements.
    Identify specific strengths, weaknesses, content gaps, and strategic differences (e.g., keyword targeting, topic depth, schema usage, internal linking patterns).
    Generate Actionable Solutions: Based solely on your analysis of the user's page and the identified competitor pages and deliver the following outputs in a clear, structured format:
    (A) Comparative On-Page SEO Gap Analysis:
    Present a clear comparison highlighting where the user's page lags behind the top competitors for key elements (Title, Headings, Content Depth/Topics, Keyword Usage, Schema, Internal Links, Meta Description). Use tables or structured lists.
    Summarize the most significant competitive disadvantages.
    (B) Prioritized Technical & Structural SEO Recommendations:
    Provide a numbered list of specific, actionable steps to improve the user page's technical and structural on-page SEO.
    Include concrete examples like optimized <title>/Meta Description suggestions, heading restructure advice, schema implementation details, and internal linking opportunities.
    (C) Section-by-Section Content Enhancement Plan:
    Analyze the existing content sections on the user's provided webpage URL.
    For each major section (or suggest new essential sections based on competitor analysis):
    Provide concrete, SEO-optimized content suggestions or rewrites.
    Focus on enhancing topic relevance, depth, clarity, keyword integration (target and semantic/LSI terms identified from analysis), and addressing content gaps.
    CRITICAL: Ensure all content suggestions are original and unique, using competitor analysis for inspiration only.
    (D) Overall Optimization Summary:
    Briefly synthesize the key findings and the most critical recommendations into a cohesive strategic statement for improving the page's ranking potential.
    Output Format:
    Present the full analysis and recommendations directly in the chat interface.
    Use clear headings, bullet points, numbered lists, and potentially tables for readability.
    Your Goal: Deliver a comprehensive, data-driven, and highly practical on-page optimization plan that the user's team can directly implement. This plan should be based on identifying the actual top competitors via search and then performing a detailed comparison using Crawl4AI to generate specific technical, structural, and content-focused recommendations aimed at improving the target webpage's SEO performance and competitive standing for the specified keyword.
    """

    # Initialize client
    client = genai.Client(api_key="AIzaSyBh74YBtp3Yo6svPZHM7xBeZql72ymDnaM")

    filename = input("Enter the filename to save (without .md extension): ") + ".md"

    try:
        # Generate content
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt,
        )

        # Get the generated text
        generated_text = response.text

        # Save to markdown file
        with open(filename, 'w', encoding='utf-8') as md_file:
            md_file.write(f"# Generated Content\n\n")
            md_file.write(f"**Response:**\n\n{generated_text}")

        print(f"\nSuccessfully saved response to '{filename}'")

        # Print preview
        print("\nPreview of generated content:")
        print(generated_text[:500] + ("..." if len(generated_text) > 500 else ""))

    except Exception as e:
        print(f"\nAn error occurred: {str(e)}")


if __name__ == "__main__":
    generate_and_save_content()