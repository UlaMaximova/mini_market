Mini Market API

API для управления мини-маркетом на FastAPI и PostgreSQL.
Быстрый старт

Предварительные требования:

    Python 3.8+

    PostgreSQL

Установка и запуск:
bash

git clone <ваш-репозиторий>
cd mini-market-api
python -m venv env
env\Scripts\activate
pip install -r requirements.txt
python create_tables.py
fastapi dev main.py

Приложение будет доступно по адресу: http://localhost:8000
Основные запросы API
Товары

    GET /products - Получить все товары

    GET /products/{id} - Получить товар по ID

Корзины

    POST /carts - Создать корзину

    GET /carts/{id} - Получить корзину по ID

    POST /carts/{id}/add_product - Добавить товар в корзину

Заказы

    POST /orders - Создать заказ

    POST /orders/{id}/confirm_payment - Подтвердить оплату

    POST /orders/{id}/cancel - Отменить заказ

Документация API: http://localhost:8000/docs
