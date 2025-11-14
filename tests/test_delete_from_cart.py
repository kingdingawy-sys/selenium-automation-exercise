import pytest
from pages.LoginPage import LoginPage
from pages.ProductPage import ProductPage
from pages.CartPage import CartPage

class TestCart:
    def test_delete_product_from_cart(self, driver):  # ← غيرت "setup" إلى "driver"
        # driver = setup  # ← نحذف السطر دا
        login_page = LoginPage(driver)
        login_page.login("valid_email@example.com", "valid_password")

        product_page = ProductPage(driver)
        product_page.add_product_to_cart(1)  # ID = 1 = Blue Top

        cart_page = CartPage(driver)
        cart_page.go_to_cart_page()
        cart_page.delete_product_from_cart("Blue Top")

        assert cart_page.is_product_not_in_cart("Blue Top") == True