import time

import pytest
from selenium.common import ElementNotVisibleException, StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait



@pytest.fixture(autouse=True)
def setup(driver):
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")

def test_explicit(driver):
    driver.find_element(By.TAG_NAME, "button").click()
    # hello_world = driver.find_element(By.ID,"finish")
    # time.sleep(10)

    hello_world = WebDriverWait(driver, 15).until(ec.visibility_of_element_located((By.ID, 'finish')))
    assert hello_world.text == "Hello World!"
    # will pass

def test_implicit(driver):
    driver.implicitly_wait(15)
    # change timeout for ALL elements when quering them with find_element/s()

    driver.find_element(By.TAG_NAME, "button").click()
    hello_world = driver.find_element(By.ID,"finish")
    assert hello_world.text == "Hello World!"
    # will fail because:
    # implicit wait only checks if element is PRESENT in DOM
    # it does NOT check if element is VISIBLE on the page

def test_element_not_on_page_without_wait(driver):
    print(len(driver.find_elements(By.ID, 'Evgen')))

def test_element_not_on_page_with_implicit_wait(driver):
    driver.implicitly_wait(15)
    driver.find_element(By.ID, 'Evgeni')
    # waits extra unnecessary 15 sec. should just fail test case

def test_element_not_on_page_with_explicit_wait(driver):
    WebDriverWait(driver, 15)\
    .until(ec.invisibility_of_element_located((By.ID,'Evgeni')))

def test_fluent_wait(driver):
    # same as explicit but with more arguments
    driver.find_element(By.TAG_NAME, "button").click()
    hello_world = WebDriverWait(driver,15,\
                                poll_frequency=1,\
                                ignored_exceptions= (ElementNotVisibleException,
                                                     StaleElementReferenceException))\
            .until(ec.element_to_be_clickable((By.ID, 'finish')))
    assert hello_world.text == "Hello World!"


