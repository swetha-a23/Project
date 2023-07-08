from models import Supplier, Stock, Consumer, Product, SupplierOrder, CustomerOrder, SupplierTransaction, ConsumerTransaction
from database import db_session
from dao import *

# Supplier Resolvers
def resolve_get_supplier_by_id(_, info, supplier_id):
    return get_supplier_by_id(supplier_id)

def resolve_get_all_suppliers(_, info):
    return get_all_suppliers()

def resolve_create_supplier(_, info, supplier_name, supplier_address, contact_number):
    return create_supplier(supplier_name, supplier_address, contact_number)

def resolve_update_supplier(_, info, supplier_id, supplier_name, supplier_address, contact_number):
    return update_supplier(supplier_id, supplier_name, supplier_address, contact_number)

def resolve_delete_supplier(_, info, supplier_id):
    return delete_supplier(supplier_id)

# Stock Resolvers
def resolve_get_stock_by_id(_, info, stock_id):
    return get_stock_by_id(stock_id)

def resolve_get_all_stock(_, info):
    return get_all_stock()

def resolve_create_stock(_, info, product_id, quantity, location):
    return create_stock(product_id, quantity, location)

def resolve_update_stock(_, info, stock_id, product_id, quantity, location):
    return update_stock(stock_id, product_id, quantity, location)

def resolve_delete_stock(_, info, stock_id):
    return delete_stock(stock_id)

# Consumer Resolvers
def resolve_get_consumer_by_id(_, info, consumer_id):
    return get_consumer_by_id(consumer_id)

def resolve_get_all_consumers(_, info):
    return get_all_consumers()

def resolve_create_consumer(_, info, consumer_name, consumer_address, contact_number):
    return create_consumer(consumer_name, consumer_address, contact_number)

def resolve_update_consumer(_, info, consumer_id, consumer_name, consumer_address, contact_number):
    return update_consumer(consumer_id, consumer_name, consumer_address, contact_number)

def resolve_delete_consumer(_, info, consumer_id):
    return delete_consumer(consumer_id)

# Product Resolvers
def resolve_get_product_by_id(_, info, product_id):
    return get_product_by_id(product_id)

def resolve_get_all_products(_, info):
    return get_all_products()

def resolve_create_product(_, info, product_name, price, description):
    return create_product(product_name, price, description)

def resolve_update_product(_, info, product_id, product_name, price, description):
    return update_product(product_id, product_name, price, description)

def resolve_delete_product(_, info, product_id):
    return delete_product(product_id)

# SupplierOrder Resolvers
def resolve_get_supplier_order_by_id(_, info, order_id):
    return get_supplier_order_by_id(order_id)

def resolve_get_all_supplier_orders(_, info):
    return get_all_supplier_orders()

def resolve_create_supplier_order(_, info, supplier_id, stock_id, order_date, quantity, total_amount):
    return create_supplier_order(supplier_id, stock_id, order_date, quantity, total_amount)

def resolve_update_supplier_order(_, info, order_id, supplier_id, stock_id, order_date, quantity, total_amount):
    return update_supplier_order(order_id, supplier_id, stock_id, order_date, quantity, total_amount)

def resolve_delete_supplier_order(_, info, order_id):
    return delete_supplier_order(order_id)

# CustomerOrder Resolvers
def resolve_get_customer_order_by_id(_, info, order_id):
    return get_customer_order_by_id(order_id)

def resolve_get_all_customer_orders(_, info):
    return get_all_customer_orders()

def resolve_create_customer_order(_, info, consumer_id, product_id, order_date, quantity, total_amount):
    return create_customer_order(consumer_id, product_id, order_date, quantity, total_amount)

def resolve_update_customer_order(_, info, order_id, consumer_id, product_id, order_date, quantity, total_amount):
    return update_customer_order(order_id, consumer_id, product_id, order_date, quantity, total_amount)

def resolve_delete_customer_order(_, info, order_id):
    return delete_customer_order(order_id)

# SupplierTransaction Resolvers
def resolve_get_supplier_transaction_by_id(_, info, transaction_id):
    return get_supplier_transaction_by_id(transaction_id)

def resolve_get_all_supplier_transactions(_, info):
    return get_all_supplier_transactions()

def resolve_create_supplier_transaction(_, info, product_id, supplier_id, transaction_date, amount):
    return create_supplier_transaction(product_id, supplier_id, transaction_date, amount)

def resolve_update_supplier_transaction(_, info, transaction_id, product_id, supplier_id, transaction_date, amount):
    return update_supplier_transaction(transaction_id, product_id, supplier_id, transaction_date, amount)

def resolve_delete_supplier_transaction(_, info, transaction_id):
    return delete_supplier_transaction(transaction_id)

# ConsumerTransaction Resolvers
def resolve_get_consumer_transaction_by_id(_, info, transaction_id):
    return get_consumer_transaction_by_id(transaction_id)

def resolve_get_all_consumer_transactions(_, info):
    return get_all_consumer_transactions()

def resolve_create_consumer_transaction(_, info, consumer_id, order_id, stock_id, transaction_date, amount):
    return create_consumer_transaction(consumer_id, order_id, stock_id, transaction_date, amount)

def resolve_update_consumer_transaction(_, info, transaction_id, consumer_id, order_id, stock_id, transaction_date, amount):
    return update_consumer_transaction(transaction_id, consumer_id, order_id, stock_id, transaction_date, amount)

def resolve_delete_consumer_transaction(_, info, transaction_id):
    return delete_consumer_transaction(transaction_id)
