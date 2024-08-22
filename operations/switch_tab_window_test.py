import time

import pytest

selenium_title = 'Selenium'
python_title = 'Welcome to Python.org'
jenkins_title = 'Jenkins'

@pytest.fixture(autouse=True)
def setup(driver):
    driver.get("https://www.selenium.dev/")

def test_switching(driver):
    selenium_handle = driver.current_window_handle
    print(selenium_handle)

#open new tab
    driver.switch_to.new_window('tab')
    driver.get('https://www.python.org/')
    python_handle = driver.current_window_handle

#open new browser
    driver.switch_to.new_window('window')
    driver.get('https://www.jenkins.io/')
    jenkins_handle = driver.current_window_handle
#switching back to windows by handles
    driver.switch_to.window(python_handle)
    time.sleep(3)
    driver.switch_to.window(selenium_handle)
    time.sleep(3)
    driver.switch_to.window(jenkins_handle)
    time.sleep(3)
#swiching by title
    switch_to_by_title(driver, python_title)
    time.sleep(3)
    switch_to_by_title(driver,selenium_title)
    time.sleep(3)
    switch_to_by_title(driver,jenkins_title)
    time.sleep(3)

def switch_to_by_title(driver, title):
    all_windows = driver.window_handles
    for handle in all_windows:
        driver.switch_to.window(handle)
        if driver.title == title:
            break