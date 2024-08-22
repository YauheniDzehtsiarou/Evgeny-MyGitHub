import time

import pytest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

# @pytest.fixture(autouse=True)
# def setup(driver):
#     driver.get("https://www.target.com/")

def test_target_search_chrome(driver):
    search_field = driver.find_element(By.ID, "search")
    search_field.send_keys("milk")
    search_field.send_keys(Keys.ENTER)
    time.sleep(5)
    driver.get("https://www.target.com/s?searchTerm=milk&tref=typeahead%7Cterm%7Cmilk%7C%7C%7Chistory")
    driver.refresh()
    # search_button = driver.find_element(By.CSS_SELECTOR, "button[aria-label='search']")
    # search_button.click()
    time.sleep(5)
    driver.refresh()
    time.sleep(7)
    driver.save_screenshot("visible_area_target_search_chrome.png")


def test_target_search_edge():
    driver = webdriver.Edge()
    driver.get("https://www.target.com/")
    search_field = driver.find_element(By.ID, "search")
    search_field.send_keys("milk")
    search_field.send_keys(Keys.ENTER)
    time.sleep(4)
    driver.refresh()
    time.sleep(4)
    full_page_text = driver.find_element(By.TAG_NAME, "body").text
    assert 'for “milk”' in full_page_text
    driver.maximize_window()
    driver.save_screenshot("visible_area_target_search_edge.png")
    driver.back()
    assert driver.current_url == "https://www.target.com/"
    driver.quit()