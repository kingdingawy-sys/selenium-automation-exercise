from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time


class ContactPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://automationexercise.com/contact_us"

        # ---- SELECTORS الحقيقية من الموقع ----
        self.name_input = (By.CSS_SELECTOR, "input[data-qa='name']")
        self.email_input = (By.CSS_SELECTOR, "input[data-qa='email']")
        self.subject_input = (By.CSS_SELECTOR, "input[data-qa='subject']")
        self.message_textarea = (By.CSS_SELECTOR, "textarea[data-qa='message']")
        self.submit_button = (By.CSS_SELECTOR, "input[data-qa='submit-button']")
        self.success_message = (By.CSS_SELECTOR, ".status.alert.alert-success")

    def go_to_contact_page(self):
        self.driver.get(self.url)
        try:
            WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located(self.name_input)
            )
        except TimeoutException:
            time.sleep(3)
            self.driver.get(self.url)
            WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located(self.name_input)
            )

    def fill_contact_form(self, name, email, subject, message):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.name_input)
        ).send_keys(name)

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.email_input)
        ).send_keys(email)

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.subject_input)
        ).send_keys(subject)

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.message_textarea)
        ).send_keys(message)

    def submit_form(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.submit_button)
        ).click()

        # التعامل مع الـ Alert
        try:
            WebDriverWait(self.driver, 5).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            alert.accept()
        except:
            pass

        # انتظار رسالة النجاح
        success_msg = WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(self.success_message)
        )

        return success_msg.text

    def is_success_message_displayed(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.success_message)
            )
            return True
        except TimeoutException:
            return False
