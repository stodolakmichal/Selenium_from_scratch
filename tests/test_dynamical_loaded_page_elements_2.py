from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

test_url = "https://the-internet.herokuapp.com/dynamic_loading/2"


def test_dynamical_loaded_page_elements_2(driver):
    driver.get(test_url)
    driver.find_elements(By.TAG_NAME, "button")[0].click()

    WebDriverWait(driver, 30).until(
        EC.text_to_be_present_in_element(
            (By.ID, "finish"),
            "Hello World!"))
    driver.quit()