import pytest
from selenium import webdriver
from pages.ProductPage import ProductPage
from pages.CartPage import CartPage

@pytest.mark.usefixtures("setup")
class TestCart:
    def test_cart_items_count_increases(self, setup):
        driver = setup
        product_page = ProductPage(driver)
        cart_page = CartPage(driver)

        # نفتح صفحة المنتجات
        product_page.go_to_products_page()

        # نروح نشوف عدد العناصر في الكارت قبل الإضافة
        cart_page.go_to_cart_page()
        initial_count = cart_page.get_cart_items_count()

        # نضيف منتج معين (مثلاً ID = 1)
        product_page.add_product_to_cart(1)

        # نروح الكارت بعد الإضافة
        cart_page.go_to_cart_page()
        new_count = cart_page.get_cart_items_count()

        print(f"Old count: {initial_count}, New count: {new_count}")
        assert new_count == initial_count + 1, "Cart items count did not increase!"
