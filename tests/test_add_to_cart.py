from pages.LoginPage import LoginPage
from pages.ProductPage import ProductPage
from pages.CartPage import CartPage

def test_add_product_to_cart(driver, email="ibrahim.mahmoud@hotmail.com", password="123456789"):
    # 1. Login
    login_page = LoginPage(driver)
    login_page.login(email, password)

    # 2. Go to product page and add to cart (استخدم id المنتج)
    product_page = ProductPage(driver)
    product_page.add_product_to_cart("1")  # مثلاً id = 1

    # 3. Go to cart and verify
    cart_page = CartPage(driver)
    cart_page.go_to_cart_page()
    # ممكن تعدل دا برضو لـ product_id لو لازم
    assert cart_page.is_product_in_cart("Blue Top") == True  # لسه بنستخدم الاسم