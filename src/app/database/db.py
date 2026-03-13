from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from src.app.models.product import Base
from src.app.models.product import Product
import os
import pandas as pd


load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=engine)

Base.metadata.create_all(bind=engine)

def load_products():

    db = SessionLocal()

    products = db.query(Product).all()

    data = [
        {
            "id": p.id,
            "name": p.name,
            "price": p.price,
            "platform": p.platform
        }
        for p in products
    ]

    db.close()

    return pd.DataFrame(data)


def save_products(df):

    db = SessionLocal()

    for _, row in df.iterrows():

        product = Product(
            name=row["name"],
            price=row["price"],
            platform=row["platform"]
        )

        print("Saving rows:", len(df))

        db.add(product)

    db.commit()
    db.close()