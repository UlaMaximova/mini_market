from typing import List

from sqlalchemy import Column, Table, Integer, String, DateTime, ForeignKey, Float
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

product_cart_association = Table(
    "product_cart_association",
    Base.metadata,
    Column("product_id", ForeignKey("products.id")),
    Column("cart_id", ForeignKey("carts.id")),
)

class Product(Base):
    __tablename__ = "products"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    quantity = Column(Integer, nullable=False)

class Cart(Base):
    __tablename__ = "carts"
    
    id = Column(Integer, primary_key=True, index=True)
    products: Mapped[List[Product]] = relationship(secondary=product_cart_association)

class Order(Base):
    __tablename__ = "orders"
    
    id = Column(Integer, primary_key=True, index=True)
    status = Column(String, nullable=False)  # waiting_payment, paid, canceled