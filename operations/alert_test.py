import time

import pytest
from selenium.webdriver.common.by import By


@pytest.fixture(autouse=True)
def setup(driver):
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")

def test_jsalert(driver):
    driver.find_element(By.XPATH, "//button[contains(text(),'Click for JS Alert')]").click()
    alert = driver.switch_to.alert
    print(alert.text)
    assert alert.text == "I am a JS Alert"
    time.sleep(4)
    alert.accept()
    time.sleep(4)


def test_jsconfirm(driver):
    driver.find_element(By.XPATH, "//button[contains(text(),'Click for JS Confirm')]").click()
    alert = driver.switch_to.alert
    alert.dismiss()