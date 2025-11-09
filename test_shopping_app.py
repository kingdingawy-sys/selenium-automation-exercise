import pytest
from shopping_app import User, Product

@pytest.mark.smoke
def test_user_login_success():
    user = User("ahmed", "123456")
    result = user.login("ahmed", "123456")
    assert result == True
    assert user.is_logged_in == True

def test_add_item_to_cart():
    user = User("ahmed", "123456")
    user.login("ahmed", "123456")
    product = Product(1, "Laptop", 1000)
    user.add_to_cart(product)
    assert user.cart.get_cart_items_count() == 1

@pytest.mark.regression
def test_add_duplicate_item():
    user = User("ahmed", "123456")
    user.login("ahmed", "123456")
    product = Product(1, "Laptop", 1000)
    user.add_to_cart(product)
    user.add_to_cart(product)
    assert user.cart.get_cart_items_count() == 2