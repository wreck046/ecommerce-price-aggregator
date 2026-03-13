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