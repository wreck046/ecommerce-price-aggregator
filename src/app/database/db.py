from sqlalchemy import create_engine
from dotenv import load_dotenv
import os
import pandas as pd

load_dotenv()

DB_URL = os.getenv("DATABASE_URL")

engine = create_engine(DB_URL)


def save_products(df):
    df.to_sql("products", engine, if_exists="append", index=False)


def load_products():
    return pd.read_sql("SELECT * FROM products", engine)