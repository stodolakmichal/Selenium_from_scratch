import time

from selenium.webdriver.common.keys import Keys

test_url = "https://the-internet.herokuapp.com/key_presses"

# Mapping keys to string
key_to_string = {
    Keys.CANCEL: "CANCEL",
    Keys.BACKSPACE: "BACK_SPACE",
    Keys.DECIMAL: "DECIMAL",
    Keys.DIVIDE: "DIVIDE",
    Keys.MULTIPLY: "MULTIPLY",
    Keys.ADD: "ADD",
    Keys.SEPARATOR: "COMMA",
    Keys.SUBTRACT: "SUBTRACT",
    Keys.SPACE: "SPACE",
    Keys.TAB: "TAB",
    Keys.CLEAR: "CLEAR",
    Keys.SHIFT: "SHIFT",
    Keys.LEFT_SHIFT: "SHIFT",
    Keys.CONTROL: "CONTROL",
    Keys.LEFT_CONTROL: "CONTROL",
    Keys.ALT: "ALT",
    Keys.LEFT_ALT: "ALT",
    Keys.PAUSE: "PAUSE",
    Keys.ESCAPE: "ESCAPE",
    Keys.PAGE_UP: "PAGE_UP",
    Keys.PAGE_DOWN: "PAGE_DOWN",
    Keys.END: "END",
    Keys.HOME: "HOME",
    Keys.LEFT: "LEFT",
    Keys.ARROW_LEFT: "LEFT",
    Keys.UP: "UP",
    Keys.ARROW_UP: "UP",
    Keys.RIGHT: "RIGHT",
    Keys.ARROW_RIGHT: "RIGHT",
    Keys.DOWN: "DOWN",
    Keys.ARROW_DOWN: "DOWN",
    Keys.INSERT: "INSERT",
    Keys.DELETE: "DELETE",
    Keys.NUMPAD0: "NUMPAD0",
    Keys.NUMPAD1: "NUMPAD1",
    Keys.NUMPAD2: "NUMPAD2",
    Keys.NUMPAD3: "NUMPAD3",
    Keys.NUMPAD4: "NUMPAD4",
    Keys.NUMPAD5: "NUMPAD5",
    Keys.NUMPAD6: "NUMPAD6",
    Keys.NUMPAD7: "NUMPAD7",
    Keys.NUMPAD8: "NUMPAD8",
    Keys.NUMPAD9: "NUMPAD9",
    Keys.MULTIPLY: "MULTIPLY",
    Keys.ADD: "ADD",
    Keys.SEPARATOR: "COMMA",
    Keys.SUBTRACT: "SUBTRACT",
    Keys.DECIMAL: "DECIMAL",
    Keys.DIVIDE: "DIVIDE",
    Keys.F1: "F1",
    Keys.F2: "F2",
    Keys.F3: "F3",
    Keys.F4: "F4",
    Keys.F5: "F5",
    Keys.F6: "F6",
    Keys.F7: "F7",
    Keys.F8: "F8",
    Keys.F9: "F9",
    Keys.F10: "F10",
    Keys.F11: "F11",
    Keys.F12: "F12"
}


def input_field_function(driver, key_press=Keys.SPACE):
    input_field = driver.find_element("id", "target")
    input_field.clear()
    input_field.send_keys(key_press)
    result = driver.find_element("id", "result")
    return result


def test_key_presses_ALL_KEYS(driver):
    driver.get(test_url)
    for key, value in key_to_string.items():
        result = input_field_function(driver, key)
        assert result.text == f"You entered: {value}", "Test failed!"
    driver.quit()