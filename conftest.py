from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import pytest
import os
from datetime import datetime, timezone

# Fixture لتشغيل المتصفح
@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()

# إعداد مجلد التقارير إذا مش موجود
REPORTS_DIR = os.path.join(os.getcwd(), "reports")
if not os.path.exists(REPORTS_DIR):
    os.makedirs(REPORTS_DIR)

# Fixture لبيانات نموذج الاتصال
@pytest.fixture
def contact_data():
    return {
        "name": "Ibrahim Tester",
        "email": f"ibrahim+{int(datetime.now(timezone.utc).timestamp())}@example.com",
        "subject": "Contact from automation test",
        "message": "This is an automated message for contact form testing."
    }

# Hook لالتقاط screenshot عند فشل التيست
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("driver")
        if driver:
            timestamp = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
            fname = os.path.join(REPORTS_DIR, f"{item.name}_{timestamp}.png")
            try:
                driver.save_screenshot(fname)
            except Exception:
                # لو في مشكلة في الحفظ، نكتب HTML للصفحة
                try:
                    html_fname = os.path.join(REPORTS_DIR, f"{item.name}_{timestamp}.html")
                    with open(html_fname, "w", encoding="utf-8") as fh:
                        fh.write(driver.page_source)
                except Exception:
                    pass
