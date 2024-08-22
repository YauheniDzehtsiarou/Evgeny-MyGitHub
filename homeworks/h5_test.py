import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


@pytest.fixture(autouse=True)
def setup(driver):
    driver.get("http://opencart.abstracta.us/index.php")


def test_sort(driver):
    driver.find_element(By.XPATH, '//li[6]/a[1]').click()
    driver.find_element(By.ID, 'list-view').click()
    dropdown = driver.find_element(By.ID, 'input-sort')
    dropdown_select = Select(dropdown)
    dropdown_select.select_by_visible_text('Price (High > Low)')
    prices = driver.find_elements(By.CLASS_NAME, 'price')
    first_item_price_after_tax = prices[0].text.split('\n')[0]
    assert first_item_price_after_tax == "$337.99"



