from selenium.webdriver.common.by import By

test_url = "https://the-internet.herokuapp.com/checkboxes"


def test_default_checkboxes(driver):
    driver.get(test_url)
    checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
    is_checkbox_0_checked = checkboxes[0].is_selected()
    is_checkbox_1_checked = checkboxes[1].is_selected()
    assert not is_checkbox_0_checked, "Checkbox 0 is checked, but shouldn't be!"
    assert is_checkbox_1_checked, "Checkbox 1 isn't checked, but should be!"


def test_if_buttons_are_clickable(driver):
    driver.get(test_url)
    checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
    for index, checkbox in enumerate(checkboxes):
        is_checkbox_selected = checkbox.is_selected()
        checkbox.click()
        if is_checkbox_selected:
            assert not checkbox.is_selected(), f"Checkbox at {index} is not clickable"
        else:
            assert checkbox.is_selected(), "Checkbox at {index} is not clickable"


def test_if_both_buttons_can_be_selected(driver):
    driver.get(test_url)
    checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
    for checkbox in checkboxes:
        if not checkbox.is_selected():
            checkbox.click()
    for checkbox in checkboxes:
        assert checkbox.is_selected()


def test_if_both_buttons_can_be_not_selected(driver):
    driver.get(test_url)
    checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
    for checkbox in checkboxes:
        if checkbox.is_selected():
            checkbox.click()
    for checkbox in checkboxes:
        assert not checkbox.is_selected()
