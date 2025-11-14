from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
import time

class ContactPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://automationexercise.com/contact_us"

        # selectors - استخدمت selectors عامة ومعقولة تبقى مستقرة
        self.name_input = (By.NAME, "name")
        self.email_input = (By.NAME, "email")
        self.subject_input = (By.NAME, "subject")
        self.message_textarea = (By.ID, "message")  # لو ID مش موجود، الكود هيفشل ويحتاج تعديل بسيط
        self.submit_button = (By.NAME, "submit")
        # رسالة النجاح المتوقعة بعد الإرسال
        self.success_message = (By.XPATH, "//*[contains(text(), 'Success') or contains(text(), 'successfully') or contains(text(), 'Success!')]")

    def go_to_contact_page(self):
        self.driver.get(self.url)
        try:
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(self.name_input)
            )
        except TimeoutException:
            # إعادة محاولة واحدة لو الصفحة بطيئة
            time.sleep(3)
            self.driver.get(self.url)
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(self.name_input)
            )

    def fill_contact_form(self, name, email, subject, message):
        # نضمن تواجد الحقول قبل الكتابة
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(self.name_input)).clear()
        self.driver.find_element(*self.name_input).send_keys(name)

        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.email_input)).clear()
        self.driver.find_element(*self.email_input).send_keys(email)

        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.subject_input)).clear()
        self.driver.find_element(*self.subject_input).send_keys(subject)

        # textarea
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.message_textarea))
        except TimeoutException:
            # fallback: try to find via name 'message' if ID not present
            self.message_textarea = (By.NAME, "message")
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.message_textarea))

        self.driver.find_element(*self.message_textarea).clear()
        self.driver.find_element(*self.message_textarea).send_keys(message)

    def submit_form(self):
        # اضغط زر الإرسال مع تأكيد أنه clickable
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.submit_button))
        submit = self.driver.find_element(*self.submit_button)
        # انقر بالجافاسكربت لضمان ثبات في CI
        self.driver.execute_script("arguments[0].click();", submit)
        # ننتظر ظهور رسالة النجاح أو قد نعيد محاولة
        try:
            WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located(self.success_message)
            )
        except TimeoutException:
            # ممكن يكون الموقع يستجيب ببطء — ننتظر شوية ونفحص يدوياً
            time.sleep(3)

    def is_success_message_displayed(self):
        try:
            return WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.success_message)
            ) is not None
        except TimeoutException:
            return False
