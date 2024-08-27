import unittest
import json
import scripts.app as app

class InventoryAPITestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.app.test_client()
        self.app.testing = True
    
    def test_add_product(self):
        # Test adding a product
        response = self.app.post('/products', data=json.dumps({
            'product_id': 1,
            'name': 'Test Product 1',
            'description': 'This is a test product',
            'price': 10.99,
            'quantity': 100
        }), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertIn('Product added successfully', response.get_data(as_text=True))

    def test_remove_product(self):
        # First add a product to remove
        self.app.post('/products', data=json.dumps({
            'product_id': 2,
            'name': 'Test Product 2',
            'description': 'This is a test product to delete',
            'price': 15.99,
            'quantity': 50
        }), content_type='application/json')
        
        # Test removing a product
        response = self.app.delete('/products/2')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Product deleted successfully', response.get_data(as_text=True))
    
    def test_update_product(self):
        # First add a product to update
        self.app.post('/products', data=json.dumps({
            'product_id': 3,
            'name': 'Test Product 3',
            'description': 'This is a test product to update',
            'price': 20.99,
            'quantity': 75
        }), content_type='application/json')
        # Test updating a product
        response = self.app.put('/products/3', data=json.dumps({
            'name': 'Updated Product 3',
            'description': 'This is an updated test product',
            'price': 25.99,
            'quantity': 50
        }), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Product updated successfully', response.get_data(as_text=True))

    def test_query_product(self):
        # First add a product to query
        self.app.post('/products', data=json.dumps({
            'product_id': 4,
            'name': 'Test Product 4',
            'description': 'This is a test product to query',
            'price': 30.99,
            'quantity': 25
        }), content_type='application/json')
        # Test querying a product
        response = self.app.get('/products/4')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['name'], 'Test Product 4')

    def test_increase_price(self):
        # First add a product to increase price
        self.app.post('/products', data=json.dumps({
            'product_id': 5,
            'name': 'Test Product 5',
            'description': 'This is a test product to increase price',
            'price': 40.99,
            'quantity': 10
        }), content_type='application/json')
        # Test increasing price of all products
        response = self.app.patch('/products/increase_price', data=json.dumps({
            'percentage': 10
        }), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Price increased successfully', response.get_data(as_text=True))
    
    def test_add_supplier(self):
        # Test adding a supplier
        response = self.app.post('/suppliers', data=json.dumps({
            'supplier_id': 1,
            'name': 'Test Supplier 1',
            'contact_info': 'test@supplier.com'
        }), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertIn('Supplier added successfully', response.get_data(as_text=True))
    
    def test_remove_supplier(self):
        # First add a supplier to remove
        self.app.post('/suppliers', data=json.dumps({
            'supplier_id': 2,
            'name': 'Test Supplier 2',
            'contact_info': 'test@supplier.com'
        }), content_type='application/json')
        # Test removing a supplier
        response = self.app.delete('/suppliers/2')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Supplier deleted successfully', response.get_data(as_text=True))

if __name__ == "__main__":
    unittest.main()