from playwright.sync_api import sync_playwright
import pandas as pd


def scrape_shopee(keyword, pages=1):

    products = []

    with sync_playwright() as p:

        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        url = f"https://shopee.co.id/search?keyword={keyword}"

        page.goto(url)
        page.wait_for_timeout(5000)

        items = page.query_selector_all("div.shopee-search-item-result__item")

        for item in items:

            try:
                name = item.query_selector("div._10Wbs-").inner_text()
                price = item.query_selector("span._29R_un").inner_text()

                price = price.replace("Rp", "").replace(".", "")

                products.append({
                    "name": name,
                    "price": int(price),
                    "platform": "Shopee"
                })

            except:
                pass

        browser.close()

    return pd.DataFrame(products)