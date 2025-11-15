from sqlalchemy import select
from sqlalchemy.orm import Session

from database import engine
from models import Product, Cart, Order


def perform_get_products():
    with Session(engine) as session:
        statement = select(Product)
        return [*session.scalars(statement)]


def perform_get_product(product_id):
    with Session(engine) as session:
        product = session.get(Product, product_id)
        return product


def perform_create_cart():
    with Session(engine) as session:
        cart = Cart()
        session.add(cart)
        session.commit()
        session.refresh(cart)
        return cart


def perform_get_cart(cart_id):
    with Session(engine) as session:
        cart = session.get(Cart, cart_id)
        cart.products # Somehow loads the relationship, otherwise products are not returned.
        return cart


def perform_add_to_cart(cart_id, product_id):
    with Session(engine) as session:
        cart = session.get(Cart, cart_id)
        product = session.get(Product, product_id)
        
        if cart and product:
            cart.products.append(product)
            session.commit()
            return True
        return False


def perform_create_order(cart_id):
    with Session(engine) as session:
        cart = session.get(Cart, cart_id)
        if cart:
            order = Order(status="waiting_payment")
            session.add(order)
            session.commit()
            session.refresh(order)
            return order
        return None


def perform_confirm_payment(order_id):
    with Session(engine) as session:
        order = session.get(Order, order_id)
        if order:
            order.status = "paid"
            session.commit()
            return True
        return False


def perform_cancel_order(order_id):
    with Session(engine) as session:
        order = session.get(Order, order_id)
        if order:
            order.status = "canceled"
            session.commit()
            return True
        return False