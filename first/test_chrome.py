from assertpy import assert_that
from selenium import webdriver


def test1():
    driver = webdriver.Chrome()
    driver.get("https://www.selenium.dev/")
    driver.maximize_window()
    assert_that(driver.title).is_equal_to("Selenium")
    driver.quit()

def test2():
    driver = webdriver.Chrome()
    driver.get("https://www.selenium.dev/")
    driver.maximize_window()
    assert driver.current_url == "https://www.selenium.dev/"
    driver.quit()

