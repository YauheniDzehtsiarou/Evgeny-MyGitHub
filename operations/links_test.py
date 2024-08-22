import pytest
from selenium.webdriver.common.by import By


@pytest.fixture(autouse=True)
def setup(driver):
    driver.get("https://www.selenium.dev/")

def test_links(driver):
    links = driver.find_elements(By.TAG_NAME,"a")
    number_of_links = len(links)
    print("Number of links on the page is", number_of_links)

    for i in range (number_of_links):
        print(i+1, links[i].text, links[i].get_attribute("href"))

def test_page_html(driver):
    print("\npage_HTML")
    print(driver.page_source)

