from selenium import webdriver
#from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import pytest
import os
from datetime import datetime, UTC

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

# folder للتقارير والصور
REPORTS_DIR = os.path.join(os.getcwd(), "reports")
os.makedirs(REPORTS_DIR, exist_ok=True)

@pytest.fixture
def contact_data():
    return {
        "name": "Ibrahim Tester",
        "email": f"ibrahim+{int(datetime.now(UTC).timestamp())}@example.com",
        "subject": "Contact from automation test",
        "message": "This is an automated message for contact form testing."
    }

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("driver")
        if driver:
            timestamp = datetime.now(UTC).strftime("%Y%m%d_%H%M%S")
            fname = os.path.join(REPORTS_DIR, f"{item.name}_{timestamp}.png")
            try:
                driver.save_screenshot(fname)
            except Exception:
                try:
                    html_fname = os.path.join(REPORTS_DIR, f"{item.name}_{timestamp}.html")
                    with open(html_fname, "w", encoding="utf-8") as fh:
                        fh.write(driver.page_source)
                except Exception:
                    pass
