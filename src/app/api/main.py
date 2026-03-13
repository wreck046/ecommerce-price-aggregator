from fastapi import FastAPI
from src.app.services.product_service import get_products

app = FastAPI()


@app.get("/products")
def products():

    return get_products()

@app.get("/search")
def search(keyword: str):

    products = get_products()

    return [p for p in products if keyword.lower() in p["name"].lower()]

@app.get("/stats")
def stats():

    products = get_products()

    prices = [p["price"] for p in products]

    return {
        "total_products": len(products),
        "avg_price": sum(prices) / len(prices) if prices else 0
    }