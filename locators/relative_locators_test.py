import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with


@pytest.fixture(autouse=True)
def setup(driver):
    driver.get("https://automationbookstore.dev/")

def test_left_of_and_below(driver):
    book = driver.find_element(
        locate_with(By.TAG_NAME, "li")
        .to_left_of(driver.find_element(By.ID, "pid6"))
        .below(driver.find_element(By.ID,"pid1"))
    )

    id = book.get_attribute("id")
    assert id == "pid5"

def test_right_of_and_above(driver):
    book = driver.find_element(
        locate_with(By.TAG_NAME,"li")
        .to_right_of(driver.find_element(By.ID, "pid1"))
        .above(driver.find_element(By.ID,"pid5"))
    )

    id = book.get_attribute("id")
    assert id == "pid2"