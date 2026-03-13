import sys
import os

sys.path.append(os.path.abspath("."))

from src.app.scraper.shopee_scraper import scrape_shopee
from src.app.database.db import save_products

keyword = input("Keyword: ")

df = scrape_shopee(keyword, pages=3)

save_products(df)

print("Data saved to database")