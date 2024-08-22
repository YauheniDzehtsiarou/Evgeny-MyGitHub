import pytest
from assertpy import assert_that

from conftest import take_screenshot


@pytest.fixture(autouse=True)
def setup(driver):
    driver.get("https://www.selenium.dev/")


def test1(driver):
    try:
        assert_that(driver.title).is_equal_to("Selenium2")
    except AssertionError:
        take_screenshot(driver)
        raise
    

def test2(driver):
    assert driver.current_url == "https://www.selenium.dev/"


