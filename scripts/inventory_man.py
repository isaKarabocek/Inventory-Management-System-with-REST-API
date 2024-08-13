class Product:
    '''
    A class to represent a product in the inventory.

    Attributes
    ----------
    product_id : int
        Unique identifier for the product.
    name : str
        Name of the product.
    description : str
        Description of the product.
    price : float
        Price of the product.
    quantity : int
        Quantity of the product in stock.
    '''
    def __init__(self, product_id, name, description, price, quantity):
        """
        Constructs all the necessary attributes for the product object.

        Parameters
        ----------
        product_id : int
            Unique identifier for the product.
        name : str
            Name of the product.
        description : str
            Description of the product.
        price : float
            Price of the product.
        quantity : int
            Quantity of the product in stock.
        """
        self.product_id = product_id
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
    
    def __repr__(self):
        """
        Returns a string representation of the product object.

        Returns
        -------
        str
            String representation of the product.
        """
        return f"Product(ID={self.product_id}, Name={self.name}, Description={self.description}, Price={self.price}, Quantity={self.quantity})"

class Supplier:
    """
    A class to represent a supplier.

    Attributes
    ----------
    supplier_id : int
        Unique identifier for the supplier.
    name : str
        Name of the supplier.
    contact_info : str
        Contact information of the supplier.
    supplied_products : list
        List of products supplied by the supplier.
    """
    def __init__ (self, supplier_id, name, contact_info):
        """
        Constructs all the necessary attributes for the supplier object.

        Parameters
        ----------
        supplier_id : int
            Unique identifier for the supplier.
        name : str
            Name of the supplier.
        contact_info : str
            Contact information of the supplier.
        """
        self.supplier_id = supplier_id
        self.name = name
        self.contact_info = contact_info
        self.supplied_products = []

        def __repr__(self):
            """
            Returns a string representation of the supplier object.

            Returns
            -------
            str
                String representation of the supplier.
            """
            return f"Supplier(ID={self.supplier_id}, Name={self.name}, Contact Info={self.contact_info})"

class Inventory:
    """
    A class to represent an inventory.

    Attributes
    ----------
    products : list
        List of products in the inventory.
    suppliers : list
        List of suppliers for the inventory.
    """
    def __init__(self):
        """
        Constructs all the necessary attributes for the inventory object.
        """
        self.products = []
        self.suppliers = []

    def add_product(self, product):
        """
        Adds a product to the inventory.

        Parameters
        ----------
        product : Product
            Product object to be added to the inventory.
        """
        self.products.append(product)

    def add_supplier(self, supplier):
        """
        Adds a supplier to the inventory.

        Parameters
        ----------
        supplier : Supplier
            Supplier object to be added to the inventory.
        """
        self.suppliers.append(supplier)

    def __repr__ (self):
        """
        Returns a string representation of the inventory object.

        Returns
        -------
        str
            String representation of the inventory.
        """
        return f"Inventory(Products={len(self.products)}, Suppliers={len(self.suppliers)})"