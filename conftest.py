#from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import pytest
import os
from datetime import datetime, UTC
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium import webdriver


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--width=1920")
    options.add_argument("--height=1080")

    service = Service()
    driver = webdriver.Firefox(service=service, options=options)
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
