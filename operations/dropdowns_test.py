import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


@pytest.fixture(autouse=True)
def setup(driver):
    driver.get("https://testpages.eviltester.com/styled/basic-html-form-test.html")

def test_dropdowns(driver):
    dropdown = driver.find_element(By.NAME, "dropdown")
    dropdown_select = Select(dropdown)
    dropdown_select.select_by_index(5)
    time.sleep(1)
    dropdown_select.select_by_visible_text("Drop Down Item 1")
    time.sleep(1)
    dropdown_select.select_by_value("dd2")
    time.sleep(2)
    selected_option_text = dropdown_select.first_selected_option.text
    assert selected_option_text == "Drop Down Item 2"

    dropdown_options = dropdown_select.options
    for option in dropdown_options:
        print(option.text)
    time.sleep(1)


def test_multiselect(driver):
    multi = driver.find_element(By.NAME, "multipleselect[]")
    multi_select = Select(multi)
    multi_select.deselect_all()
    multi_select.select_by_index(0)
    multi_select.select_by_index(1)

    time.sleep(1)