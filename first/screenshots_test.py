from Screenshot import Screenshot
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_screenshot_of_visible_area():
    driver = webdriver.Edge()
    driver.get("https://www.selenium.dev/")
    driver.maximize_window()
    driver.save_screenshot("visible_area_chrome.png")
    driver.quit()


def test_screenshot_of_full_page_firefox():
    driver = webdriver.Firefox()
    driver.get("https://www.selenium.dev/")
    driver.maximize_window()
    driver.save_full_page_screenshot("full_page_firefox.png")
    driver.quit()


def test_screenshot_of_full_page_chrome():
    driver = webdriver.Edge()
    driver.get("https://www.selenium.dev/",)
    driver.maximize_window()
    ob = Screenshot.Screenshot()
    ob.full_screenshot(driver,'.',"full_page_chrome.png",)
    driver.quit()


def test_screenshot_of_web_element():
    driver = webdriver.Edge()
    driver.get("https://www.selenium.dev/")
    driver.maximize_window()
    logo = driver.find_element(By.ID, "selenium_webdriver")
    screenshot = logo.screenshot_as_png
    with open("logo.png", "wb") as file:
        file.write(screenshot)
    driver.quit()
