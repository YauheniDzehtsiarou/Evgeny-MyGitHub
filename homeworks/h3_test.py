import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


@pytest.fixture(autouse=True)
def setup(driver):
    driver.get("https://duckduckgo.com/")


def test_search(driver):
    driver.find_element(By.ID, "searchbox_input").send_keys("maven", Keys.ENTER)
    assert driver.find_element(By.ID, "search_form_input").get_attribute("value") == 'maven'
    maven_links = driver.find_elements(By.PARTIAL_LINK_TEXT, "Apache Maven")
    assert len(maven_links) > 0
    print("\ntotal number of links containing 'Apache Maven' is", len(maven_links))




