# product.py
# Application file


class Product:

    def __init__(self, name, price):
        # Step 1: Store the product data
        self.name = name
        self.price = price

    def get_price(self):
        # Step 2: Return the stored price
        return self.price
