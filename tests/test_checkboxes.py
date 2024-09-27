from selenium.webdriver.common.by import By

test_url = "https://the-internet.herokuapp.com/checkboxes"


def test_default_checkboxes(driver):
    driver.get(test_url)
    checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
    is_checkbox_0_checked = checkboxes[0].is_selected()
    is_checkbox_1_checked = checkboxes[1].is_selected()
    assert not is_checkbox_0_checked, "Checkbox 0 is checked, but shouldn't be!"
    assert is_checkbox_1_checked, "Checkbox 1 isn't checked, but should be!"
