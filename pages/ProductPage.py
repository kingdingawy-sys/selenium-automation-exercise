from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
import time

class ProductPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://automationexercise.com/products"

    def go_to_products_page(self):
        """يفتح صفحة المنتجات وينتظر تحميلها بثبات"""
        self.driver.get(self.url)
        try:
            WebDriverWait(self.driver, 25).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".productinfo"))
            )
        except TimeoutException:
            # نعيد المحاولة مرة واحدة في حالة بطء الموقع
            time.sleep(5)
            self.driver.get(self.url)
            WebDriverWait(self.driver, 25).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".productinfo"))
            )

    def click_add_to_cart(self, product_id):
        """يضغط زر Add to Cart باستخدام JavaScript لضمان الثبات"""
        xpath = f"//a[@data-product-id='{product_id}' and contains(@class, 'add-to-cart')]"
        try:
            add_button = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, xpath))
            )
            self.driver.execute_script("arguments[0].click();", add_button)
            time.sleep(3)
        except (TimeoutException, StaleElementReferenceException):
            # إعادة المحاولة لو العنصر لسه مش clickable
            time.sleep(5)
            add_button = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, xpath))
            )
            self.driver.execute_script("arguments[0].click();", add_button)
            time.sleep(3)

    def add_product_to_cart(self, product_id):
        """عملية كاملة لإضافة المنتج"""
        self.go_to_products_page()
        self.click_add_to_cart(product_id)
