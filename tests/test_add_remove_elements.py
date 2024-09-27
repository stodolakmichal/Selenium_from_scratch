from selenium.webdriver.common.by import By

test_url = "https://the-internet.herokuapp.com/add_remove_elements/"


def add_elements(driver):
    for _ in range(3):
        driver.find_element(By.CSS_SELECTOR, "button[onclick='addElement()']").click()


def test_add_elements(driver):
    """Test that the elements are added to the page."""
    driver.get(test_url)
    add_elements(driver)

    assert len(driver.find_elements(By.CLASS_NAME, "added-manually")) == 3
    driver.quit()


def test_remove_elements(driver):
    """Test that the elements are removed from the page."""
    driver.get(test_url)
    add_elements(driver)

    for _ in range(2):
        driver.find_element(By.CSS_SELECTOR, "button[onclick='deleteElement()']").click()

    assert len(driver.find_elements(By.CLASS_NAME, "added-manually")) == 1
    driver.quit()
