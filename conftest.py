import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def driver():
    # 1. Set up the Chrome driver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # ← مهم جدًا
    chrome_options.add_argument("--no-sandbox")  # ← مهم جدًا
    chrome_options.add_argument("--disable-dev-shm-usage")  # ← مهم جدًا
    chrome_options.add_argument("--disable-gpu")  # ← مهم جدًا
    chrome_options.add_argument("--window-size=1920,1080")  # ← حجم الشاشة
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    yield driver
    driver.quit()


    # 2. Give the driver to the test

    # 3. After the test finishes, close the driver


@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()




