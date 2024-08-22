import time

import pytest
from selenium.webdriver.common.by import By


@pytest.fixture(autouse=True)
def setup(driver):
    driver.get("https://testpages.eviltester.com/styled/basic-html-form-test.html")

def test_element_states(driver):
    time.sleep(3)
    radio_button = driver.find_element(By.XPATH, "//input[@value='rd1']")
    assert radio_button.is_displayed()
    radio_button.click()
    assert radio_button.is_selected()

def test_read_input(driver):
    user = driver.find_element(By.NAME, "username")
    user.send_keys("Evgeny")
    input = user.get_attribute("value")
    assert input=="Evgeny"
    time.sleep(4)
