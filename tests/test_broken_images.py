import pytest
from selenium.webdriver.common.by import By
import requests

test_url = "https://the-internet.herokuapp.com/broken_images"


@pytest.mark.skip
def test_broken_images(driver):
    """Test that the images are not broken."""
    driver.get(test_url)
    images = driver.find_elements(By.TAG_NAME, "img")

    for image in images:
        img_src = image.get_attribute("src")
        response = requests.get(img_src)
        assert response.status_code == 200, f"Broken image: {img_src}"
    driver.quit()
