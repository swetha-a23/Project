from models import Supplier, Stock, Consumer, Product, SupplierOrder, CustomerOrder, SupplierTransaction, ConsumerTransaction
from database import db_session
import re

# DAO functions for Supplier
def get_supplier_by_id(supplier_id):
    return db_session.query(Supplier).filter(Supplier.supplier_id == supplier_id).first()

def get_all_suppliers():
    return db_session.query(Supplier).all()

def create_supplier(supplier_name, supplier_address, contact_number):
    # Validate contact_number using a regular expression
    if not re.match(r'^\d{10}$', str(contact_number)):
        raise ValueError("Invalid contact number")

    supplier = Supplier(supplier_name=supplier_name, supplier_address=supplier_address, contact_number=contact_number)
    db_session.add(supplier)
    db_session.commit()
    return supplier

def update_supplier(supplier_id, supplier_name, supplier_address, contact_number):
    supplier = get_supplier_by_id(supplier_id)
    if supplier:
        supplier.supplier_name = supplier_name
        supplier.supplier_address = supplier_address
        supplier.contact_number = contact_number
        db_session.commit()
    return supplier

def delete_supplier(supplier_id):
    supplier = get_supplier_by_id(supplier_id)
    if supplier:
        db_session.delete(supplier)
        db_session.commit()
    return supplier

# DAO functions for Stock
def get_stock_by_id(stock_id):
    return db_session.query(Stock).filter(Stock.stock_id == stock_id).first()

def get_all_stock():
    return db_session.query(Stock).all()

def create_stock(product_id, quantity, location):
    # Validate quantity using a regular expression
    if not re.match(r'^\d+$', str(quantity)):
        raise ValueError("Invalid quantity")

    stock = Stock(product_id=product_id, quantity=quantity, location=location)
    db_session.add(stock)
    db_session.commit()
    return stock

def update_stock(stock_id, product_id, quantity, location):
    stock = get_stock_by_id(stock_id)
    if stock:
        stock.product_id = product_id
        stock.quantity = quantity
        stock.location = location
        db_session.commit()
    return stock


def delete_stock(stock_id):
    stock = get_stock_by_id(stock_id)
    if stock:
        db_session.delete(stock)
        db_session.commit()
    return stock

# DAO functions for Consumer
def get_consumer_by_id(consumer_id):
    return db_session.query(Consumer).filter(Consumer.consumer_id == consumer_id).first()

def get_all_consumers():
    return db_session.query(Consumer).all()

def create_consumer(consumer_name, consumer_address, contact_number):
    # Validate contact_number using a regular expression
    if not re.match(r'^\d{10}$', str(contact_number)):
        raise ValueError("Invalid contact number")

    consumer = Consumer(consumer_name=consumer_name, consumer_address=consumer_address, contact_number=contact_number)
    db_session.add(consumer)
    db_session.commit()
    return consumer

def update_consumer(consumer_id, consumer_name, consumer_address, contact_number):
    consumer = get_consumer_by_id(consumer_id)
    if consumer:
        consumer.consumer_name = consumer_name
        consumer.consumer_address = consumer_address
        consumer.contact_number = contact_number
        db_session.commit()
    return consumer

def delete_consumer(consumer_id):
    consumer = get_consumer_by_id(consumer_id)
    if consumer:
        db_session.delete(consumer)
        db_session.commit()
    return consumer

# DAO functions for Product
def get_product_by_id(product_id):
    return db_session.query(Product).filter(Product.product_id == product_id).first()

def get_all_products():
    return db_session.query(Product).all()

def create_product(product_name, price, description):
    # Validate product_name using a regular expression
    if not re.match(r'^[A-Za-z0-9\s]+$', product_name):
        raise ValueError("Invalid product name")

    product = Product(product_name=product_name, price=price, description=description)
    db_session.add(product)
    db_session.commit()
    return product

def update_product(product_id, product_name, price, description):
    product = get_product_by_id(product_id)
    if product:
        product.product_name = product_name
        product.price = price
        product.description = description
        db_session.commit()
    return product

def delete_product(product_id):
    product = get_product_by_id(product_id)
    if product:
        db_session.delete(product)
        db_session.commit()
    return product

# DAO functions for SupplierOrder
def get_supplier_order_by_id(order_id):
    return db_session.query(SupplierOrder).filter(SupplierOrder.order_id == order_id).first()

def get_all_supplier_orders():
    return db_session.query(SupplierOrder).all()

def create_supplier_order(supplier_id, stock_id, order_date, quantity, total_amount):
    # Validate quantity and total_amount using regular expressions
    if not re.match(r'^\d+$', str(quantity)):
        raise ValueError("Invalid quantity")
    if not re.match(r'^\d+$', str(total_amount)):
        raise ValueError("Invalid total amount")

    supplier_order = SupplierOrder(supplier_id=supplier_id, stock_id=stock_id, order_date=order_date, quantity=quantity, total_amount=total_amount)
    db_session.add(supplier_order)
    db_session.commit()
    return supplier_order

def update_supplier_order(order_id, supplier_id, stock_id, order_date, quantity, total_amount):
    supplier_order = get_supplier_order_by_id(order_id)
    if supplier_order:
        supplier_order.supplier_id = supplier_id
        supplier_order.stock_id = stock_id
        supplier_order.order_date = order_date
        supplier_order.quantity = quantity
        supplier_order.total_amount= total_amount
        db_session.commit()
    return supplier_order

def delete_supplier_order(order_id):
    supplier_order = get_supplier_order_by_id(order_id)
    if supplier_order:
        db_session.delete(supplier_order)
        db_session.commit()
    return supplier_order

# DAO functions for CustomerOrder
def get_customer_order_by_id(order_id):
    return db_session.query(CustomerOrder).filter(CustomerOrder.order_id == order_id).first()

def get_all_customer_orders():
    return db_session.query(CustomerOrder).all()

def create_customer_order(consumer_id, product_id, order_date, quantity, total_amount):
    # Validate quantity and total_amount using regular expressions
    if not re.match(r'^\d+$', str(quantity)):
        raise ValueError("Invalid quantity")
    if not re.match(r'^\d+$', str(total_amount)):
        raise ValueError("Invalid total amount")

    customer_order = CustomerOrder(consumer_id=consumer_id, product_id=product_id, order_date=order_date, quantity=quantity, total_amount=total_amount)
    db_session.add(customer_order)
    db_session.commit()
    return customer_order

def update_customer_order(order_id, consumer_id, product_id, order_date,  quantity, total_amount):
    customer_order = get_customer_order_by_id(order_id)
    if customer_order:
        customer_order.consumer_id = consumer_id
        customer_order.product_id = product_id
        customer_order.order_date = order_date
        customer_order.quantity = quantity
        customer_order.total_amount = total_amount
        db_session.commit()
    return customer_order

def delete_customer_order(order_id):
    customer_order = get_customer_order_by_id(order_id)
    if customer_order:
        db_session.delete(customer_order)
        db_session.commit()
    return customer_order

# DAO functions for SupplierTransaction
def get_supplier_transaction_by_id(transaction_id):
    return db_session.query(SupplierTransaction).filter(SupplierTransaction.transaction_id == transaction_id).first()

def get_all_supplier_transactions():
    return db_session.query(SupplierTransaction).all()

def create_supplier_transaction(product_id, supplier_id, transaction_date, amount):
    # Validate amount using a regular expression
    if not re.match(r'^\d+(\.\d{1,2})?$', str(amount)):
        raise ValueError("Invalid amount")

    supplier_transaction = SupplierTransaction(product_id=product_id, supplier_id=supplier_id, transaction_date=transaction_date, amount=amount)
    db_session.add(supplier_transaction)
    db_session.commit()
    return supplier_transaction

def update_supplier_transaction(transaction_id, product_id, supplier_id, transaction_date, amount):
    supplier_transaction = get_supplier_transaction_by_id(transaction_id)
    if supplier_transaction:
        supplier_transaction.product_id = product_id
        supplier_transaction.supplier_id = supplier_id
        supplier_transaction.transaction_date = transaction_date
        supplier_transaction.amount = amount
        db_session.commit()
    return supplier_transaction

def delete_supplier_transaction(transaction_id):
    supplier_transaction = get_supplier_transaction_by_id(transaction_id)
    if supplier_transaction:
        db_session.delete(supplier_transaction)
        db_session.commit()
    return supplier_transaction


# DAO functions for ConsumerTransaction
def get_consumer_transaction_by_id(transaction_id):
    return db_session.query(ConsumerTransaction).filter(ConsumerTransaction.transaction_id == transaction_id).first()

def get_all_consumer_transactions():
    return db_session.query(ConsumerTransaction).all()

def create_consumer_transaction(consumer_id, order_id, stock_id, transaction_date, amount):
    # Validate amount using a regular expression
    if not re.match(r'^\d+(\.\d{1,2})?$', str(amount)):
        raise ValueError("Invalid amount")

    consumer_transaction = ConsumerTransaction(consumer_id=consumer_id, order_id=order_id, stock_id=stock_id, transaction_date=transaction_date, amount=amount)
    db_session.add(consumer_transaction)
    db_session.commit()
    return consumer_transaction

def update_consumer_transaction(transaction_id, consumer_id, order_id, stock_id, transaction_date, amount):
    consumer_transaction = get_consumer_transaction_by_id(transaction_id)
    if consumer_transaction:
        consumer_transaction.consumer_id = consumer_id
        consumer_transaction.order_id = order_id
        consumer_transaction.stock_id = stock_id
        consumer_transaction.transaction_date = transaction_date
        consumer_transaction.amount = amount
        db_session.commit()
    return consumer_transaction

def delete_consumer_transaction(transaction_id):
    consumer_transaction = get_consumer_transaction_by_id(transaction_id)
    if consumer_transaction:
        db_session.delete(consumer_transaction)
        db_session.commit()
    return consumer_transaction





    