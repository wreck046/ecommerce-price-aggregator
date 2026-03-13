from playwright.sync_api import sync_playwright
import pandas as pd


def scrape_shopee(keyword, pages=1):

    products = []

    with sync_playwright() as p:

        browser = p.chromium.launch(headless=False)

        context = browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        )

        page = context.new_page()

        # buka homepage dulu
        page.goto("https://shopee.co.id")
        page.wait_for_timeout(5000)

        # buka halaman search
        search_url = f"https://shopee.co.id/search?keyword={keyword}"
        page.goto(search_url)

        page.wait_for_timeout(6000)

        # scroll untuk load produk
        for _ in range(pages):

            page.mouse.wheel(0, 9000)
            page.wait_for_timeout(2000)

        # selector produk (lebih stabil)
        items = page.query_selector_all("div.col-xs-2-4")

        print("Items found:", len(items))

        for item in items:

            try:

                name_el = item.query_selector("div._10Wbs-")
                price_el = item.query_selector("span._29R_un")

                if name_el and price_el:

                    name = name_el.inner_text()
                    price = price_el.inner_text()

                    price = price.replace("Rp", "").replace(".", "")

                    products.append({
                        "name": name,
                        "price": int(price),
                        "platform": "Shopee"
                    })

            except Exception:
                pass

        browser.close()

    return pd.DataFrame(products)