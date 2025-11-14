# tests/test_contact.py
import pytest
import random
import string
from pages.ContactPage import ContactPage

def random_email():
    rnd = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    return f"test_{rnd}@example.com"

class TestContact:
    def test_contact_form_submission(self, driver):
        """
        اختبار ارسال فورم الاتصال والتحقق من ظهور رسالة نجاح
        """
        contact = ContactPage(driver)
        contact.go_to_contact_page()

        name = "Ibrahim Tester"
        email = random_email()
        subject = "Automation Test Contact"
        message = "Hello from automated test. This is a test message."

        contact.fill_contact_form(name, email, subject, message)
        contact.submit_form()

        assert contact.is_success_message_displayed() == True, "Expected success message after contact form submission"
