from selenium import webdriver
from selenium.webdriver.edge.options import Options


def test_remote():
    server_url = 'http://10.0.0.150:4444'
    browser_options = Options()
    browser_options.set_capability("platformName", 'Windows 10')

    driver = webdriver.Remote(command_executor = server_url, options = browser_options)
    driver.get('https://www.selenium.dev/')
    assert driver.title == "Selenium"

    driver.quit()
