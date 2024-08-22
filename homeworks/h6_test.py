import time

import pytest
from selenium.webdriver.common.by import By


@pytest.fixture(autouse=True)
def setup(driver_firefox):
    driver_firefox.get("https://www.target.com/")


def switch_to_by_title(driver, title):
    all_windows = driver.window_handles
    for handle in all_windows:
        driver.switch_to.window(handle)
        if driver.title == title:
            break


def test_target(driver):
    driver.find_element(By.LINK_TEXT, 'Privacy policy').click()
    switch_to_by_title(driver, 'Target Privacy Policy : Target')
    assert len(driver.find_elements(By.XPATH, "//h1[contains(text(),'Target Privacy Policy')]")) > 0
    driver.close()
    switch_to_by_title(driver, "Target : Expect More. Pay Less.")
    assert driver.title == "Target : Expect More. Pay Less."


def test_target_firefox(driver_firefox):
    driver_firefox.find_element(By.LINK_TEXT, 'Privacy policy').click()
    switch_to_by_title(driver_firefox, 'Target Privacy Policy : Target')
    time.sleep(1)
    assert len(driver_firefox.find_elements(By.XPATH, "//h1[contains(text(),'Target Privacy Policy')]")) > 0
    driver_firefox.close()
    switch_to_by_title(driver_firefox, "Target : Expect More. Pay Less.")
    assert driver_firefox.title == "Target : Expect More. Pay Less."