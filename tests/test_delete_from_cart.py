import pytest
from selenium import webdriver
from pages.ProductPage import ProductPage
from pages.CartPage import CartPage

@pytest.mark.usefixtures("setup")
class TestCart:
    def test_delete_product_from_cart(self, setup):
        driver = setup
        product_page = ProductPage(driver)
        cart_page = CartPage(driver)

        # نضيف منتج معين الأول
        product_page.add_product_to_cart(2)
        cart_page.go_to_cart_page()

        # نتأكد إنه فعلاً في الكارت
        assert cart_page.is_product_in_cart("Men Tshirt"), "Product not found in cart before deletion."

        # نحذف المنتج
        cart_page.delete_product_from_cart("Men Tshirt")

        # نتأكد إنه اتمسح
        assert cart_page.is_product_not_in_cart("Men Tshirt"), "Product still appears in cart after deletion."
