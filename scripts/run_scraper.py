from src.app.scraper.aggregator import scrape_all
from src.app.services.product_service import save_products

keyword = input("Keyword: ")
pages = int(input("Pages to scrape: "))

df = scrape_all(keyword, pages)

print("Total rows:", len(df))

save_products(df)

print("Data saved to database")