# main.py
from fastapi import FastAPI, HTTPException, Body

from models import Product, Cart, Order
from database_requests import (
    perform_get_products,
    perform_get_product,
    perform_create_cart,
    perform_get_cart,
    perform_add_to_cart,
    perform_create_order,
    perform_confirm_payment,
    perform_cancel_order
)

app = FastAPI(title="Mini Market API", version="1.0")

@app.get("/")
def root():
    return {"message": "Mini Market API"}

@app.get("/products")
def get_products():
    """Получить все товары"""
    return perform_get_products()

@app.get("/products/{product_id}")
def get_product(product_id):
    """Получить конкретный товар"""
    product = perform_get_product(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Товар не найден")
    return product

@app.post("/carts")
def create_cart():
    """Создать корзину"""
    cart = perform_create_cart()
    return {"cart_id": cart.id}

@app.get("/carts/{cart_id}")
def get_cart(cart_id):
    """Получить корзину"""
    cart = perform_get_cart(cart_id)
    if not cart:
        raise HTTPException(status_code=404, detail="Корзина не найдена")
    return cart

@app.post("/carts/{cart_id}/add_product")
def add_to_cart(cart_id, request=Body()):
    """Добавить товар в корзину"""
    cart = perform_get_cart(cart_id)
    if not cart:
        raise HTTPException(status_code=404, detail="Корзина не найдена")
    
    product = perform_get_product(request['product_id'])
    if not product:
        raise HTTPException(status_code=404, detail="Товар не найден")
    
    success = perform_add_to_cart(cart_id, request['product_id'])

    if success:
        return {"status": "Товар добавлен в корзину"}
    else:
        raise HTTPException(status_code=400, detail="Ошибка при добавлении товара в корзину")

@app.post("/orders")
def create_order(request=Body()):
    """Создать заказ"""
    cart = perform_get_cart(request['cart_id'])
    if not cart:
        raise HTTPException(status_code=404, detail="Корзина не найдена")
    
    order = perform_create_order(request['cart_id'])
    if order:
        return {"order_id": order.id}
    else:
        raise HTTPException(status_code=400, detail="Ошибка при создании заказа")

@app.post("/orders/{order_id}/confirm_payment")
def confirm_payment(order_id):
    """Подтвердить оплату заказа"""
    success = perform_confirm_payment(order_id)
    if success:
        return {"status": "Оплата подтверждена"}
    else:
        raise HTTPException(status_code=404, detail="Заказ не найден")

@app.post("/orders/{order_id}/cancel")
def cancel_order(order_id):
    """Отменить заказ"""
    success = perform_cancel_order(order_id)
    if success:
        return {"status": "Заказ отменен"}
    else:
        raise HTTPException(status_code=404, detail="Заказ не найден")