from src.app.database.db import SessionLocal
from src.app.models.product import Product


def save_products(df):

    db = SessionLocal()

    for _, row in df.iterrows():

        product = Product(
            name=row["name"],
            price=row["price"],
            platform=row["platform"]
        )

        db.add(product)

    db.commit()
    db.close()


def get_products():

    db = SessionLocal()

    products = db.query(Product).all()

    result = [
        {
            "id": p.id,
            "name": p.name,
            "price": p.price,
            "platform": p.platform
        }
        for p in products
    ]

    db.close()

    return result