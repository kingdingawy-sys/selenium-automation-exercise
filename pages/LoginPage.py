from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://automationexercise.com/login"

    def go_to_login_page(self):
        self.driver.get(self.url)

    def enter_email(self, email):
        email_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, "email"))
        )
        email_field.send_keys(email)

    def enter_password(self, password):
        password_field = self.driver.find_element(By.NAME, "password")
        password_field.send_keys(password)

    def click_login_button(self):
        login_button = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        login_button.click()

    def login(self, email, password):
        self.go_to_login_page()
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_button()