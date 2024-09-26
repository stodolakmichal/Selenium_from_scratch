import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_argument("--headless=new")
driver = webdriver.Chrome(options=options)
url = "https://the-internet.herokuapp.com/entry_ad"
driver.get(url)
driver.implicitly_wait(10)


def test_is_browser_ready():
    assert driver.title == "The Internet", "Browser is not ready!"


def test_is_ad_displayed():
    ad = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "modal")))
    assert ad.is_displayed(), "AD is not displayed!"


def test_is_modal_text_displayed():
    modal_text = driver.find_element(By.CLASS_NAME, "modal-body")
    assert modal_text.is_displayed(), "Modal text is not displayed!"


def test_is_modal_title_displayed():
    modal_title = driver.find_element(By.CLASS_NAME, "modal-title")
    assert modal_title.is_displayed(), "Modal title is not displayed!"


def test_closing_ad():
    ad = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "modal")))
    close_ad_button = driver.find_element(By.CLASS_NAME, "modal-footer")
    close_ad_button.click()
    assert not ad.is_displayed(), "Ad is not closed"


def test_restart_ad():
    close_restart_ad_button = driver.find_element(By.ID, "restart-ad")
    close_restart_ad_button.click()
    ad = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "modal")))
    assert ad.is_displayed(), "AD not restarted"
