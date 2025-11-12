from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://automationexercise.com/view_cart"

    def go_to_cart_page(self):
        self.driver.get(self.url)
        # نتاكد إن الصفحة حملت
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".cart_info"))
        )

    def is_product_in_cart(self, product_name):
        try:
            # نشوف في العنصر اللي بيبقى فيه الاسم (h4/a)
            product_locator = (By.XPATH, f"//h4/a[contains(text(), '{product_name}')]")
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(product_locator)
            )
            print(f"Product '{product_name}' found in cart!")
            return True
        except:
            print(f"Product '{product_name}' NOT found in cart.")
            return False

    def delete_product_from_cart(self, product_name):
        # نستخدم XPath بناءً على DevTools
        # الزر اللي بيبقى جنب المنتج دا
        xpath = f"//h4/a[contains(text(), '{product_name}')]/../../..//a[@class='cart_quantity_delete']"
        delete_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, xpath))
        )
        delete_button.click()
        time.sleep(2)  # نخلي السلة تتحديث

    def is_product_not_in_cart(self, product_name):
        try:
            # نحاول نلاقيه، لو لقيناه نرجع False
            product_locator = (By.XPATH, f"//h4/a[contains(text(), '{product_name}')]")
            self.driver.find_element(*product_locator)
            print(f"Product '{product_name}' is STILL in cart!")
            return False  # لقيناه، يبقي مش صح
        except:
            print(f"Product '{product_name}' is NOT in cart anymore!")
            return True   # مالقيناش، يبقي صح

    def get_cart_items_count(self):
        try:
            # نلاقي عدد الصفوف في الجدول (كل صف = منتج)
            rows = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".cart_info tbody tr"))
            )
            count = len(rows)
            print(f"Items in cart: {count}")
            return count
        except:
            print("Cart is empty or could not load items.")
            return 0