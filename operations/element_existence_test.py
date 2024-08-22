import pytest
from selenium.webdriver.common.by import By


@pytest.fixture(autouse=True)
def setup(driver):
    driver.get('https://www.selenium.dev/selenium/docs/api/py/api.html')

def test_element_existence(driver):
    list_of_elements = driver.find_elements(By.NAME, "q")
    assert len(list_of_elements) == 1

    list_of_elements = driver.find_elements(By.ID, "evgeny")
    assert len(list_of_elements) == 0
