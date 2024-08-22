import pytest
from selenium.webdriver.common.by import By


@pytest.fixture(autouse=True)
def setup(driver):
    driver.get("https://demo.guru99.com/test/social-icon.html")

def test_tooltip(driver):
    fb = driver.find_element(By.XPATH, "//body/div[@id='page']/div[2]/div[1]/a[5]")
    tooltip = fb.get_attribute('title')
    print(tooltip)
    assert tooltip == "Facebook"