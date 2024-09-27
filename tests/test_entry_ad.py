from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

test_url = "https://the-internet.herokuapp.com/entry_ad"


def open_browser_and_wait_for_ad(driver):
    driver.get(test_url)
    ad = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "modal")))
    return ad


def test_is_browser_ready(driver):
    open_browser_and_wait_for_ad(driver)
    assert driver.title == "The Internet", "Browser is not ready!"


def test_is_ad_displayed(driver):
    ad = open_browser_and_wait_for_ad(driver)
    assert ad.is_displayed(), "AD is not displayed!"


def test_is_modal_text_displayed(driver):
    open_browser_and_wait_for_ad(driver)
    modal_text = driver.find_element(By.CLASS_NAME, "modal-body")
    assert modal_text.is_displayed(), "Modal text is not displayed!"


def test_is_modal_title_displayed(driver):
    open_browser_and_wait_for_ad(driver)
    modal_title = driver.find_element(By.CLASS_NAME, "modal-title")
    assert modal_title.is_displayed(), "Modal title is not displayed!"


def test_closing_ad(driver):
    ad = open_browser_and_wait_for_ad(driver)
    close_ad_button = driver.find_element(By.CLASS_NAME, "modal-footer")
    close_ad_button.click()
    assert not ad.is_displayed(), "Ad is not closed"


def test_restart_ad(driver):
    open_browser_and_wait_for_ad(driver)
    close_ad_button = driver.find_element(By.CLASS_NAME, "modal-footer")
    close_ad_button.click()
    close_restart_ad_button = driver.find_element(By.ID, "restart-ad")
    close_restart_ad_button.click()
    ad = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "modal")))
    assert ad.is_displayed(), "AD not restarted"
