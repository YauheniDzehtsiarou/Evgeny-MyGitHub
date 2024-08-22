import datetime
import os.path
from pathlib import Path
import pytest
from selenium import webdriver
from datetime import datetime
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from pages.LoginPage import LoginPage


@pytest.fixture
def driver():
    # browser = os.environ.get("Browser")
    # operation_system =  os.environ.get("OS")
    # print(f"browser = {browser}, os= {operation_system}")
    browser = "Chrome"
    match browser:
        case "Chrome":
            # options are needed to bypass chrome security restrictions
            options = webdriver.ChromeOptions()
            options.add_experimental_option('excludeSwitches', ['enable-logging'])
            chrome_driver = webdriver.Chrome(options)
            chrome_driver.maximize_window()
            yield chrome_driver
            chrome_driver.quit()
        case "Firefox":
            firefox_driver = webdriver.Firefox()
            firefox_driver.maximize_window()
            yield firefox_driver
            firefox_driver.quit()

@pytest.fixture
def driver_firefox():
    firefox_driver = webdriver.Firefox()
    firefox_driver.maximize_window()
    yield firefox_driver
    firefox_driver.quit()


@pytest.fixture
def login_page():
    # options are needed to bypass chrome security restrictions
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    chrome_driver = webdriver.Chrome(options)
    chrome_driver.maximize_window()
    yield LoginPage(chrome_driver)
    chrome_driver.quit()

def take_screenshot(driver):
    current_datetime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    Path('screenshots').mkdir(parents=True, exist_ok= True)
    driver.save_screenshot(os.path.join("screenshots",f'scr{current_datetime}.png'))

def click_element(driver, locator):
    WebDriverWait(driver, 15).until(ec.element_to_be_clickable(locator)).click()