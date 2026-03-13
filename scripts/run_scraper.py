from src.app.scraper.shopee_scraper import scrape_shopee
from src.app.services.product_service import save_products

keyword = input("Keyword: ")
pages = int(input("Pages to scrape: "))

df = scrape_shopee(keyword, pages)

print("Total rows:", len(df))

save_products(df)

print("Data saved to database")