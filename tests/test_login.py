from pages.LoginPage import LoginPage

def test_successful_login(driver):
    # 1. Create an object of LoginPage, giving it the driver
    login_page = LoginPage(driver)

    # 2. Use the login method with valid credentials
    login_page.login("ibrahim.mahmoud@hotmail.com", "123456789")

    # 3. Assert that the login was successful
    # For example, check if a specific text appears on the page after login
    # This text should be something that appears only when logged in
    assert "Logged in as" in driver.page_source