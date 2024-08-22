import time

import pytest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

@pytest.fixture(autouse=True)
def setup(driver):
    driver.get("https://www.target.com/")


def test_target_registry(driver):
    registry_button = driver.find_element(By.ID, "utilityNav-registries")
    registry_button.click()
    find_registry_button = driver.find_element(By.XPATH, "//button[contains(text(),'Find a registry')]")
    find_registry_button.click()
    time.sleep(4)
    assert driver.title == "Search Results : Gift Registry : Target"
    full_page_text = driver.find_element(By.TAG_NAME, "body").text
    assert "Find a registry" in full_page_text




