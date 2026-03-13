import pandas as pd

from src.app.scraper.shopee_scraper import scrape_shopee
from src.app.scraper.tokopedia_scraper import scrape_tokopedia


def scrape_all(keyword, pages):

    df1 = scrape_shopee(keyword, pages)
    df2 = scrape_tokopedia(keyword, pages)

    df = pd.concat([df1, df2], ignore_index=True)

    return df