import time
from telnetlib import EC

import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

test_url = "https://the-internet.herokuapp.com/challenging_dom"


def test_page_load(driver):
    """Test that the page loads correctly."""
    driver.get(test_url)
    assert "The Internet" in driver.title
    assert driver.find_element(By.CSS_SELECTOR, ".example > h3").text == "Challenging DOM"
    driver.quit()


def test_buttons(driver):
    """Test that the page has 3 buttons and that they work."""
    driver.get(test_url)
    buttons = driver.find_elements(By.CSS_SELECTOR, ".large-2.columns .button")
    assert len(buttons) == 3
    for button_number in range(len(buttons)):
        button = driver.find_elements(By.CSS_SELECTOR, ".large-2.columns .button")[button_number]
        ActionChains(driver).move_to_element(button).click(button).perform()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".example > h3")))
        assert driver.find_element(By.CSS_SELECTOR, ".example > h3").text == "Challenging DOM"

    driver.quit()