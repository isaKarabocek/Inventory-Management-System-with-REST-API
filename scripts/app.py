import sys
import os

# Add the path to the scripts folder
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from flask import Flask, request, jsonify
from scripts.inventory_man import Inventory, Product, Supplier

app = Flask(__name__)

# Initialize the inventory
inventory = Inventory()

@app.route('/products', methods=['POST'])
def add_product():
    """
    Add a product to the inventory.
    """
    data = request.get_json()
    product_id = data['product_id']
    name = data['name']
    description = data['description']
    price = data['price']
    quantity = data['quantity']

    product = Product(product_id, name, description, price, quantity)
    inventory.add_product(product)

    return jsonify({"message": "Product added successfully"}), 201

@app.route('/products/<int:product_id>', methods=['DELETE'])
def remove_product(product_id):
    """
    Delete a product from the inventory.
    """
    for product in inventory.products:
        if product.product_id == product_id:
            inventory.products.remove(product)
            return jsonify({"message": "Product deleted successfully"}), 200

    return jsonify({"message": "Product not found"}), 404

@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    """
    Update a product in the inventory.
    """
    data = request.get_json()
    name = data['name']
    description = data['description']
    price = data['price']
    quantity = data['quantity']

    for product in inventory.products:
        if product.product_id == product_id:
            product.name = name
            product.description = description
            product.price = price
            product.quantity = quantity
            return jsonify({"message": "Product updated successfully"}), 200

    return jsonify({"message": "Product not found"}), 404

@app.route('/products/<int:product_id>', methods=['GET'])
def query_product(product_id):
    """
    Get details of a product in the inventory.
    """
    for product in inventory.products:
        if product.product_id == product_id:
            return jsonify({
                "product_id": product.product_id,
                "name": product.name,
                "description": product.description,
                "price": product.price,
                "quantity": product.quantity
            }), 200

    return jsonify({"message": "Product not found"}), 404

@app.route('/products/increase_price', methods=['PATCH'])
def increase_price():
    """
    Increase the price of all products in the inventory.
    """
    percentage = request.json['percentage']
    for product in inventory.products:
        product.price *= (1 + percentage / 100)
    return jsonify({"message": "Price increased successfully"}), 200

@app.route('/suppliers', methods=['POST'])
def add_supplier():
    """
    Add a supplier to the inventory.
    """
    data = request.get_json()
    supplier = Supplier(data['supplier_id'], data['name'], data['contact_info'])
    inventory.add_supplier(supplier)

    return jsonify({"message": "Supplier added successfully"}), 201

@app.route('/suppliers/<int:supplier_id>', methods=['DELETE'])
def remove_supplier(supplier_id):
    """
    Delete a supplier from the inventory.
    """
    result = inventory.remove_supplier(supplier_id)
    if result:
        return jsonify({"message": "Supplier deleted successfully"}), 200
    else:
        return jsonify({"message": "Supplier not found"}), 404


if __name__ == '__main__':
    app.run(debug=True)