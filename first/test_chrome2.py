import pytest
from assertpy import assert_that



@pytest.fixture(autouse=True)
def setup(driver):
    driver.get("https://www.selenium.dev/")


def test1(driver):
    assert_that(driver.title).is_equal_to("Selenium2")


def test2(driver):
    assert driver.current_url == "https://www.selenium.dev/"


