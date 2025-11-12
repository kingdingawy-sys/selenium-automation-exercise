from pages.LoginPage import LoginPage
from pages.ProductPage import ProductPage
from pages.CartPage import CartPage

def test_add_another_product_to_cart(driver, email="ibrahim.mahmoud@hotmail.com", password="123456789"):
    # 1. Login
    login_page = LoginPage(driver)
    login_page.login(email, password)

    # 2. Go to product page and add product ID = 2
    product_page = ProductPage(driver)
    product_page.add_product_to_cart("2")  # ID = 2

    # 3. Go to cart and verify
    cart_page = CartPage(driver)
    cart_page.go_to_cart_page()
    # نستخدم اسم المنتج ID = 2 (مثلاً "Polo Top")
    assert cart_page.is_product_in_cart("Men Tshirt") == True































