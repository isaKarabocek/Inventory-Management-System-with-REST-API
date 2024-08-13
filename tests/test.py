import sys
import os

# Add the path to the scripts folder
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from scripts.inventory_man import Product, Supplier, Inventory

def test_inventory():
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

    # Check if products and supplier are added
    assert len(inventory.products) == 2
    assert len(inventory.suppliers) == 1

    # Check the representation of the inventory
    assert repr(inventory) == "Inventory(Products=2, Suppliers=1)"

    # Print the actual representation of the product
    print(repr(product1))

    # Check the representation of the product
    assert repr(product1) == "Product(ID=1, Name=Widget, Price=10.0, Quantity=100)"

    # Check the representation of the supplier
    assert repr(supplier) == "Supplier(ID=1, Name=SupplierCo, Contact=supplier@example.com)"

    print("All tests passed!")

if __name__ == "__main__":
    test_inventory()