import sys
import os
import unittest

# Add the path to the scripts folder
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from scripts.inventory_man import Product, Supplier, Inventory

class TestInventory(unittest.TestCase):

    def test_add_and_check_inventory(self):
        # Create an inventory
        inventory = Inventory()

        # Create some products
        product1 = Product(1, "Widget", "A simple widget", 10.0, 100)
        product2 = Product(2, "Gadget", "An advanced gadget", 20.0, 50)

        # Create a supplier
        supplier = Supplier(1, "SupplierCo", "supplier@example.com")

        # Add products and supplier to the inventory
        inventory.add_product(product1)
        inventory.add_product(product2)
        inventory.add_supplier(supplier)

        # Test 1: Check if the products and supplier are added to the inventory
        self.assertEqual(len(inventory.products), 2)
        self.assertEqual(len(inventory.suppliers), 1)

        # Check the representation of the inventory
        self.assertEqual(repr(inventory), "Inventory(Products=2, Suppliers=1)")

        # Check the representation of the product
        self.assertEqual(repr(product1), "Product(ID=1, Name=Widget, Description=A simple widget, Price=10.0, Quantity=100)")

        # Check the representation of the supplier
        self.assertEqual(repr(supplier), "Supplier(ID=1, Name=SupplierCo, Contact Info=supplier@example.com)")

    def test_save_and_load_inventory(self):
        # Create an inventory
        inventory = Inventory()

        # Create some products
        product1 = Product(1, "Widget", "A simple widget", 10.0, 100)
        product2 = Product(2, "Gadget", "An advanced gadget", 20.0, 50)

        # Create a supplier
        supplier = Supplier(1, "SupplierCo", "supplier@example.com")

        # Add products and supplier to the inventory
        inventory.add_product(product1)
        inventory.add_product(product2)
        inventory.add_supplier(supplier)

        # Save the inventory to CSV     
        inventory.save_to_csv('test_products.csv', 'test_suppliers.csv')

        # Create a new inventory and load data from CSV
        new_inventory = Inventory()
        new_inventory.load_from_csv('test_products.csv', 'test_suppliers.csv')

        # Test 2: Check if the products and supplier are loaded from the CSV files
        self.assertEqual(len(new_inventory.products), 2)
        self.assertEqual(len(new_inventory.suppliers), 1)
        self.assertEqual(repr(new_inventory.products[0]), repr(product1))
        self.assertEqual(repr(new_inventory.products[1]), repr(product2))

        # Clean up the test files
        os.remove('test_products.csv')
        os.remove('test_suppliers.csv')

        
if __name__ == "__main__":
    unittest.main()