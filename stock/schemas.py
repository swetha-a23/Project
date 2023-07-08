import strawberry
from typing import List
from datetime import datetime
from resolvers import *
from dao import *

# Supplier Schema
@strawberry.type
class SupplierSchema:
    supplier_id: int
    supplier_name: str
    supplier_address: str
    contact_number: str

# Stock Schema
@strawberry.type
class StockSchema:
    stock_id: int
    product_id: int
    quantity: int
    location: str

# Consumer Schema
@strawberry.type
class ConsumerSchema:
    consumer_id: int
    consumer_name: str
    consumer_address: str
    contact_number: str

# Product Schema
@strawberry.type
class ProductSchema:
    product_id: int
    product_name: str
    price: float
    description: str

# SupplierOrder Schema
@strawberry.type
class SupplierOrderSchema:
    order_id: int
    supplier_id: int
    stock_id: int
    order_date: datetime
    quantity: int
    total_amount: int

# CustomerOrder Schema
@strawberry.type
class CustomerOrderSchema:
    order_id: int
    consumer_id: int
    product_id: int
    order_date: datetime
    quantity: int
    total_amount: int

# SupplierTransaction Schema
@strawberry.type
class SupplierTransactionSchema:
    transaction_id: int
    product_id: int
    supplier_id: int
    transaction_date: datetime
    amount: float

# ConsumerTransaction Schema
@strawberry.type
class ConsumerTransactionSchema:
    transaction_id: int
    consumer_id: int
    order_id: int
    stock_id: int
    transaction_date: datetime
    amount: float

# Query Schema
@strawberry.type
class Query:
    @strawberry.field
    def getAllSuppliers(self) -> List[SupplierSchema]:
        return get_all_suppliers()

    @strawberry.field
    def getSupplierById(self, supplier_id: int) -> SupplierSchema:
        return get_supplier_by_id(supplier_id)

    @strawberry.field
    def getAllStocks(self) -> List[StockSchema]:
        return get_all_stock()

    @strawberry.field
    def getStockById(self, stock_id: int) -> StockSchema:
        return get_stock_by_id(stock_id)

    @strawberry.field
    def getAllConsumers(self) -> List[ConsumerSchema]:
        return get_all_consumers()

    @strawberry.field
    def getConsumerById(self, consumer_id: int) -> ConsumerSchema:
        return get_consumer_by_id(consumer_id)

    @strawberry.field
    def getAllProducts(self) -> List[ProductSchema]:
        return get_all_products()

    @strawberry.field
    def getProductById(self, product_id: int) -> ProductSchema:
        return get_product_by_id(product_id)

    @strawberry.field
    def getAllSupplierOrders(self) -> List[SupplierOrderSchema]:
        return get_all_supplier_orders()

    @strawberry.field
    def getSupplierOrderById(self, order_id: int) -> SupplierOrderSchema:
        return get_supplier_order_by_id(order_id)

    @strawberry.field
    def getAllCustomerOrders(self) -> List[CustomerOrderSchema]:
        return get_all_customer_orders()

    @strawberry.field
    def getCustomerOrderById(self, order_id: int) -> CustomerOrderSchema:
        return get_customer_order_by_id(order_id)

    @strawberry.field
    def getAllSupplierTransactions(self) -> List[SupplierTransactionSchema]:
        return get_all_supplier_transactions()

    @strawberry.field
    def getSupplierTransactionById(self, transaction_id : int) -> SupplierTransactionSchema:
        return get_supplier_transaction_by_id(transaction_id)

    @strawberry.field
    def getAllConsumerTransactions(self) -> List[ConsumerTransactionSchema]:
        return get_all_consumer_transactions()

    @strawberry.field
    def getConsumerTransactionById(self, transaction_id: int) -> ConsumerTransactionSchema:
        return get_consumer_transaction_by_id(transaction_id)

# Mutation Schema
@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_supplier(supplier_name: str, supplier_address: str, contact_number: str) -> SupplierSchema:
        return create_supplier(supplier_name, supplier_address, contact_number)

    @strawberry.mutation
    def update_supplier(supplier_id: int, supplier_name: str, supplier_address: str, contact_number: str) -> SupplierSchema:
        return update_supplier(supplier_id, supplier_name, supplier_address, contact_number)

    @strawberry.mutation
    def delete_supplier(supplier_id: int) -> SupplierSchema:
        return delete_supplier(supplier_id)

    @strawberry.mutation
    def create_stock(product_id: int, quantity: int, location: str) -> StockSchema:
        return create_stock(product_id, quantity, location)

    @strawberry.mutation
    def update_stock(stock_id: int, product_id: int, quantity: int, location: str) -> StockSchema:
        return update_stock(stock_id, product_id, quantity, location)

    @strawberry.mutation
    def delete_stock(stock_id: int) -> StockSchema:
        return delete_stock(stock_id)

    @strawberry.mutation
    def create_consumer(consumer_name: str, consumer_address: str, contact_number: str) -> ConsumerSchema:
        return create_consumer(consumer_name, consumer_address, contact_number)

    @strawberry.mutation
    def update_consumer(consumer_id: int, consumer_name: str, consumer_address: str, contact_number: str) -> ConsumerSchema:
        return update_consumer(consumer_id, consumer_name, consumer_address, contact_number)

    @strawberry.mutation
    def delete_consumer(consumer_id: int) -> ConsumerSchema:
        return delete_consumer(consumer_id)

    @strawberry.mutation
    def create_product(product_name: str, price: float, description: str) -> ProductSchema:
        return create_product(product_name, price, description)

    @strawberry.mutation
    def update_product(product_id: int, product_name: str, price: float, description: str) -> ProductSchema:
        return update_product(product_id, product_name, price, description)

    @strawberry.mutation
    def delete_product(product_id: int) -> ProductSchema:
        return delete_product(product_id)

    @strawberry.mutation
    def create_supplier_order(supplier_id: int, stock_id: int, order_date: datetime, quantity: int, total_amount: int) -> SupplierOrderSchema:
        return create_supplier_order(supplier_id, stock_id, order_date, quantity, total_amount)

    @strawberry.mutation
    def update_supplier_order(order_id: int, supplier_id: int, stock_id: int, order_date: datetime, quantity: int, total_amount:int) -> SupplierOrderSchema:
        return update_supplier_order(order_id, supplier_id, stock_id, order_date, quantity, total_amount)

    @strawberry.mutation
    def delete_supplier_order(order_id: int) -> SupplierOrderSchema:
        return delete_supplier_order(order_id)

    @strawberry.mutation
    def create_customer_order(consumer_id: int, product_id: int, order_date: datetime, quantity: int, total_amount: int) -> CustomerOrderSchema:
        return create_customer_order(consumer_id, product_id, order_date, quantity, total_amount)

    @strawberry.mutation
    def update_customer_order(order_id: int, consumer_id: int, product_id: int, order_date: datetime, quantity: int, total_amount: int) -> CustomerOrderSchema:
        return update_customer_order(order_id, consumer_id, product_id, order_date, quantity, total_amount)

    @strawberry.mutation
    def delete_customer_order(order_id: int) -> CustomerOrderSchema:
        return delete_customer_order(order_id)

    @strawberry.mutation
    def create_supplier_transaction(product_id: int, supplier_id: int, transaction_date: datetime, amount: float) -> SupplierTransactionSchema:
        return create_supplier_transaction(product_id, supplier_id, transaction_date, amount)

    @strawberry.mutation
    def update_supplier_transaction(transaction_id: int, product_id: int, supplier_id: int, transaction_date: datetime, amount: float) -> SupplierTransactionSchema:
        return update_supplier_transaction(transaction_id, product_id, supplier_id, transaction_date, amount)

    @strawberry.mutation
    def delete_supplier_transaction(transaction_id: int) -> SupplierTransactionSchema:
        return delete_supplier_transaction(transaction_id)

    @strawberry.mutation
    def create_consumer_transaction(consumer_id: int, order_id: int, stock_id: int, transaction_date: datetime, amount: float) -> ConsumerTransactionSchema:
        return create_consumer_transaction(consumer_id, order_id, stock_id, transaction_date, amount)

    @strawberry.mutation
    def update_consumer_transaction(transaction_id: int, consumer_id: int, order_id: int, stock_id: int, transaction_date: datetime, amount: float) -> ConsumerTransactionSchema:
        return update_consumer_transaction(transaction_id, consumer_id, order_id, stock_id, transaction_date, amount)

    @strawberry.mutation
    def delete_consumer_transaction(transaction_id: int) -> ConsumerTransactionSchema:
        return delete_consumer_transaction(transaction_id)


# Define the GraphQL schema
schema = strawberry.Schema(query=Query, mutation=Mutation)
