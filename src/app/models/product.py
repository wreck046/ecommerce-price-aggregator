from sqlalchemy import Column, Integer, String
from src.app.database.base import Base


class Product(Base):

    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    price = Column(Integer)
    platform = Column(String)