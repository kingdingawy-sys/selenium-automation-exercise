from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.LoginPage import LoginPage


def test_login_failure(driver):
    login_page = LoginPage(driver)
    # بيانات خاطئة
    login_page.login("wrong_email@example.com", "wrong_password")

    # 1. نشوف لو ظهرت رسالة خطأ (نستخدم try-except)
    try:
        # نستخدم CSS Selector (مثلاً)
        error_message = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".alert.alert-danger"))
        )
        # نتاكد إن فيها نص معين
        assert "Invalid" in error_message.text or "error" in error_message.text
    except:
        # 2. لو مالقينش رسالة، نشوف URL
        # لو لسه في صفحة تسجيل دخول، يبقى فعلاً ماسجّلش
        assert "login" in driver.current_url