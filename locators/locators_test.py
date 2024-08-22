import time

import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


@pytest.fixture(autouse=True)
def setup(driver):
    driver.get("http://opencart.abstracta.us/")

def test_locators(driver):
#1 class name
    driver.find_element(By.CLASS_NAME,"swiper-button-next").click()
    time.sleep(3)

#2 element name
    driver.find_element(By.NAME,"search").send_keys("MacBook", Keys.ENTER)
    time.sleep(3)

#3 id
    driver.find_element(By.ID, "cart-total").click()
    time.sleep(3)

#4 css selector
    driver.find_element(By.CSS_SELECTOR, ".btn.btn-default.btn-lg").click()
    time.sleep(3)

#5 link text
    driver.find_element(By.LINK_TEXT, "Your Store").click()
    time.sleep(3)

#6 partial link text
    driver.find_element(By.PARTIAL_LINK_TEXT, "PDAs").click()
    time.sleep(3)

#7 tag name
    visible_text = driver.find_element(By.TAG_NAME, "body").text
    print(visible_text)
    time.sleep(3)

#8 XPath
    driver.find_element(By.XPATH, "//div[1]/div[1]/div[2]/div[2]/button[1]/span[1]").click()
    time.sleep(3)



