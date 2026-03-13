from playwright.sync_api import sync_playwright
import pandas as pd


def scrape_tokopedia(keyword, pages=1):

    products = []

    with sync_playwright() as p:

        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        url = f"https://www.tokopedia.com/search?q={keyword}"

        page.goto(url)

        page.wait_for_timeout(6000)

        for _ in range(pages):
            page.mouse.wheel(0, 8000)
            page.wait_for_timeout(2000)

        items = page.query_selector_all('[data-testid="divSRPContentProducts"] div')

        for item in items:

            try:

                name = item.query_selector("span").inner_text()
                price = item.query_selector("div.css-rhd610").inner_text()

                price = price.replace("Rp", "").replace(".", "")

                products.append({
                    "name": name,
                    "price": int(price),
                    "platform": "Tokopedia"
                })

            except:
                pass

        browser.close()

    return pd.DataFrame(products)