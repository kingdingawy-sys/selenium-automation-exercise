class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.is_logged_in = False
        self.cart = Cart()

    def login(self, entered_username, entered_password):
        if entered_username == self.username and entered_password == self.password:
            self.is_logged_in = True
            return True
        else:
            return False

    def add_to_cart(self, product):
        if self.is_logged_in:
            self.cart.add_product(product)
        else:
            raise Exception("User must be logged in to add items to cart")


class Product:
    def __init__(self, product_id, name, price):
        self.id = product_id
        self.name = name
        self.price = price


class Cart:
    def __init__(self):
        self.items = {}

    def add_product(self, product):
        if product.id in self.items:
            self.items[product.id] += 1
        else:
            self.items[product.id] = 1

    def get_cart_items_count(self):
        total = 0
        for quantity in self.items.values():
            total += quantity
        return total