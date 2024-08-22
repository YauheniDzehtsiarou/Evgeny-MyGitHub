import time

from selenium import webdriver

from utils.read_config import read_property

browser = "edge"

def get_driver():
    browser = read_property()
    match browser:
        case "chrome":
            return webdriver.Chrome()
        case "firefox":
            return webdriver.Firefox()
        case "edge":
            return webdriver.Edge()

def test_multibrowsers():
    driver = get_driver()
    driver.get("https://www.selenium.dev/")
    driver.maximize_window()
    assert driver.title == "Selenium"
    assert driver.current_url == "https://www.selenium.dev/"
    print("Browser:", driver.name)
    time.sleep(4)
    driver.quit()