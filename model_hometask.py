from datetime import datetime
from pony.orm import *


db = Database(provider="sqlite", filename="myshop.sqlite", create_db=True)


class Product(db.Entity):
    """Товар"""
    category = Required('Category')
    title = Required(str)
    description = Optional(str)
    unit = Required(str)
    price = Required(float)
    # alt_categories = Set('Category')
    # amount = int # сколько товаров в магазине сейчас
    history = Set('ProductHistory')
    cartitem = Set('CartItem')
    orderitem = Required('OrderItem')


class ProductHistory(db.Entity):
    product = Required('Product')
    created = Optional(datetime, default=datetime.now)
    price = Required(float)


class Category(db.Entity):
    """Категория товара"""
    parent = Set('Category', reverse='parent')
    title = Required(str)
    products = Set(Product)


class Customer(db.Entity):
    """Покупатель"""
    id = PrimaryKey(int, auto=True)
    email = Required(str)
    phone = Required(str)
    name = Required(str)
    address = Set('Address')
    cart = Required('Cart')
    order = Optional('Order')


class Address(db.Entity):
    """Адрес"""
    customer = Required(Customer)
    country = Required(str)
    city = Required(str)
    street = Required(str)
    zip_code = Required(str)
    house = Required(int)


class Cart(db.Entity):
    """Корзина с товарами"""
    customer = Optional(Customer)
    products = Set('CartItem')


class CartItem(db.Entity):
    """Элемент корзины"""
    cart = Required(Cart)
    product = Required(Product)
    amount = Optional(int)  # 1 единица тавара


class Order(db.Entity):
    """Заказ"""
    customer = Optional(Customer)
    created = Optional(datetime)
    products = Set('OrderItem')
    status = Required('Status')


class Status(db.Entity):
    """Статус"""
    name = Required(str)
    order = Optional(Order)


class OrderItem(db.Entity):
    """Товар (одна позиция) в заказе"""
    order = Required(Order)
    product = Optional(Product)
    amount = Optional(int)


# class Menu(db.Entity):
#     """Меню"""

def set_sql_debug():
    pass

sql_debug(True)

db.generate_mapping(create_tables=True)


@db_session
def populate_database():
    client1 = Customer(email='kirill_vercetti@itmo.com', phone='+78121234567',
                       name='Kirill Vercetti')

    client2 = Customer(email='donald.trump@whitehouse.com', phone='+1666666',
                       name='Donald Trump')

    prod1 = Product(title='"Russia - generous soul!"', description='Chocolate "Russia"',
                       unit='1 pc', price=100.0)

    cat1 = Category(title='Choco')


    db.commit()


@db_session
def test_queries():
    print('All customers')
    result = select(c for c in Customer)[:]
    print(result)
