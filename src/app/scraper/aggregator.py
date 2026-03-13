import pandas as pd

from src.app.scraper.shopee_scraper import scrape_shopee
from src.app.scraper.tokopedia_scraper import scrape_tokopedia


def scrape_all(keyword, pages):

    df1 = scrape_shopee(keyword, pages)
    print("Shopee rows:", len(df1))

    df2 = scrape_tokopedia(keyword, pages)
    print("Tokopedia rows:", len(df2))

    df = pd.concat([df1, df2], ignore_index=True)
    print("Total combined rows:", len(df))

    if df.empty:
        print("Scraper gagal, menggunakan fallback dataset...")
        df = fallback_products()

    return df

def fallback_products():

    data = [
        {"name": "Kemeja Koko Pria", "price": 120000, "platform": "Shopee"},
        {"name": "Kemeja Koko Katun", "price": 95000, "platform": "Tokopedia"},
        {"name": "Kemeja Koko Modern", "price": 150000, "platform": "Shopee"}
    ]
    return pd.DataFrame(data)