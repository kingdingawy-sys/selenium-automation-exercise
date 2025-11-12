from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class ProductPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://automationexercise.com/products"

    def go_to_products_page(self):
        self.driver.get(self.url)
        # نتاكد إن الصفحة حملت
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".productinfo"))
        )

    def click_add_to_cart(self, product_id):
        # نستخدم XPath بناءً على DevTools
        xpath = f"//a[@data-product-id='{product_id}' and contains(@class, 'add-to-cart')]"
        add_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, xpath))
        )
        # نشوف لو ظهرت رسالة "added to cart"
        self.driver.execute_script("arguments[0].click();", add_button)  # نضغط بالجافا سكريبت
        time.sleep(3)  # نخلي الرسالة تظهر

    def add_product_to_cart(self, product_id):
        self.go_to_products_page()
        self.click_add_to_cart(product_id)