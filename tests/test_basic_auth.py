from selenium.webdriver.common.by import By

test_url = "https://the-internet.herokuapp.com/basic_auth/"


def basic_auth(driver):
    """Test that the user can log in with basic authentication."""
    user = "admin"
    password = "admin"
    url_with_credentials = f"https://{user}:{password}@the-internet.herokuapp.com/basic_auth"
    driver.get(url_with_credentials)
    assert driver.find_element(By.CSS_SELECTOR, "p").text == "Congratulations! You must have the proper credentials."
    driver.quit()
