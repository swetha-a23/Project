import unittest
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app import app
from schemas import schema
from strawberry.test import client
from dao import *
from models import Consumer, Supplier, Product, SupplierOrder, Stock

class APITestCase(unittest.TestCase):
    def setUp(self):
        # Create a test Flask app and configure it
        self.app = Flask(__name__)
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
        self.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

        # Create a test database
        self.db = SQLAlchemy(self.app)
        self.db.create_all()

        # Set up the GraphQL client for testing
        self.client = client(schema)

    def tearDown(self):
        # Clean up the test database
        self.db.session.remove()
        self.db.drop_all()

    def test_consumer_dao_functions(self):
        # Create a consumer
        consumer = create_consumer("Consumer 1", "Address 1", "1234567890")
        self.assertIsNotNone(consumer)
        self.assertEqual(consumer.consumer_name, "Consumer 1")
        self.assertEqual(consumer.consumer_address, "Address 1")
        self.assertEqual(consumer.contact_number, "1234567890")

        # Get consumer by ID
        retrieved_consumer = get_consumer_by_id(consumer.consumer_id)
        self.assertEqual(retrieved_consumer, consumer)

        # Update consumer
        updated_consumer = update_consumer(consumer.consumer_id, "Updated Consumer", "Updated Address", "9876543210")
        self.assertIsNotNone(updated_consumer)
        self.assertEqual(updated_consumer.consumer_name, "Updated Consumer")
        self.assertEqual(updated_consumer.consumer_address, "Updated Address")
        self.assertEqual(updated_consumer.contact_number, "9876543210")

        # Delete consumer
        deleted_consumer = delete_consumer(consumer.consumer_id)
        self.assertIsNotNone(deleted_consumer)
        self.assertEqual(deleted_consumer.consumer_id, consumer.consumer_id)

        # Get all consumers
        all_consumers = get_all_consumers()
        self.assertEqual(len(all_consumers), 0)

    def test_supplier_dao_functions(self):
        # Create a supplier
        supplier = create_supplier("Supplier 1", "Address 1", "1234567890")
        self.assertIsNotNone(supplier)
        self.assertEqual(supplier.supplier_name, "Supplier 1")
        self.assertEqual(supplier.supplier_address, "Address 1")
        self.assertEqual(supplier.contact_number, "1234567890")

        # Get supplier by ID
        retrieved_supplier = get_supplier_by_id(supplier.supplier_id)
        self.assertEqual(retrieved_supplier, supplier)

        # Update supplier
        updated_supplier = update_supplier(supplier.supplier_id, "Updated Supplier", "Updated Address", "9876543210")
        self.assertIsNotNone(updated_supplier)
        self.assertEqual(updated_supplier.supplier_name, "Updated Supplier")
        self.assertEqual(updated_supplier.supplier_address, "Updated Address")
        self.assertEqual(updated_supplier.contact_number, "9876543210")

        # Delete supplier
        deleted_supplier = delete_supplier(supplier.supplier_id)
        self.assertIsNotNone(deleted_supplier)
        self.assertEqual(deleted_supplier.supplier_id, supplier.supplier_id)

        # Get all suppliers
        all_suppliers = get_all_suppliers()
        self.assertEqual(len(all_suppliers), 0)

    def test_product_dao_functions(self):
        # Create a product
        product = create_product("Product 1", 10, "Description 1")
        self.assertIsNotNone(product)
        self.assertEqual(product.product_name, "Product 1")
        self.assertEqual(product.price, 10)
        self.assertEqual(product.description, "Description 1")

        # Get product by ID
        retrieved_product = get_product_by_id(product.product_id)
        self.assertEqual(retrieved_product, product)

        # Update product
        updated_product = update_product(product.product_id, "Updated Product", 20, "Updated Description")
        self.assertIsNotNone(updated_product)
        self.assertEqual(updated_product.product_name, "Updated Product")
        self.assertEqual(updated_product.price, 20)
        self.assertEqual(updated_product.description, "Updated Description")

        # Delete product
        deleted_product = delete_product(product.product_id)
        self.assertIsNotNone(deleted_product)
        self.assertEqual(deleted_product.product_id, product.product_id)

        # Get all products
        all_products = get_all_products()
        self.assertEqual(len(all_products), 0)

    def test_supplier_order_dao_functions(self):
        # Create a supplier
        supplier = create_supplier("Supplier 1", "Address 1", "1234567890")

        # Create a product
        product = create_product("Product 1", 10, "Description 1")

        # Create a supplier order
        supplier_order = create_supplier_order(supplier.supplier_id, product.product_id, "2023-07-07", 5, 50)
        self.assertIsNotNone(supplier_order)
        self.assertEqual(supplier_order.supplier_id, supplier.supplier_id)
        self.assertEqual(supplier_order.product_id, product.product_id)
        self.assertEqual(supplier_order.order_date, "2023-07-07")
        self.assertEqual(supplier_order.quantity, 5)
        self.assertEqual(supplier_order.total_amount, 50)

        # Get supplier order by ID
        retrieved_supplier_order = get_supplier_order_by_id(supplier_order.order_id)
        self.assertEqual(retrieved_supplier_order, supplier_order)

        # Update supplier order
        updated_supplier_order = update_supplier_order(supplier_order.order_id, supplier.supplier_id, product.product_id, "2023-07-08", 10, 100)
        self.assertIsNotNone(updated_supplier_order)
        self.assertEqual(updated_supplier_order.order_date, "2023-07-08")
        self.assertEqual(updated_supplier_order.quantity, 10)
        self.assertEqual(updated_supplier_order.total_amount, 100)

        # Delete supplier order
        deleted_supplier_order = delete_supplier_order(supplier_order.order_id)
        self.assertIsNotNone(deleted_supplier_order)
        self.assertEqual(deleted_supplier_order.order_id, supplier_order.order_id)

        # Get all supplier orders
        all_supplier_orders = get_all_supplier_orders()
        self.assertEqual(len(all_supplier_orders), 0)

    def test_stock_dao_functions(self):
        # Create a product
        product = create_product("Product 1", 10, "Description 1")

        # Create a stock
        stock = create_stock(product.product_id, 50, "Location 1")
        self.assertIsNotNone(stock)
        self.assertEqual(stock.product_id, product.product_id)
        self.assertEqual(stock.quantity, 50)
        self.assertEqual(stock.location, "Location 1")

        # Get stock by ID
        retrieved_stock = get_stock_by_id(stock.stock_id)
        self.assertEqual(retrieved_stock, stock)

        # Update stock
        updated_stock = update_stock(stock.stock_id, product.product_id, 100, "Updated Location")
        self.assertIsNotNone(updated_stock)
        self.assertEqual(updated_stock.quantity, 100)
        self.assertEqual(updated_stock.location, "Updated Location")

        # Delete stock
        deleted_stock = delete_stock(stock.stock_id)
        self.assertIsNotNone(deleted_stock)
        self.assertEqual(deleted_stock.stock_id, stock.stock_id)

        # Getall stock
        all_stock = get_all_stock()
        self.assertEqual(len(all_stock), 0)

if __name__ == '__main__':
    unittest.main()
