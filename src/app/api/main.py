from fastapi import FastAPI, Query
from src.app.database.db import load_products

app = FastAPI()


@app.get("/products")
def get_products():

    df = load_products()

    return df.to_dict(orient="records")


@app.get("/search")
def search_products(keyword: str = Query(...)):

    df = load_products()

    result = df[df["name"].str.contains(keyword, case=False, na=False)]

    return result.to_dict(orient="records")