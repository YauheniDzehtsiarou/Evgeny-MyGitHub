import time
import pytest
from selenium.webdriver.common.by import By


@pytest.fixture(autouse=True)
def setup(driver):
    driver.get("http://www.uitestingplayground.com/dynamictable")


def test_search(driver):
    column_name = "Network"
    table_rows = driver.find_elements(By.XPATH, "//div[@role='row']")

    #print table headers
    table_headers = table_rows[0].text.split()
    print()
    print(*table_headers)

    #print number of rows
    print("\nnumber of rows in the table is", len(table_rows))

    #print column given a column name

    time.sleep(3)
    column_index = table_headers.index(column_name)
    for row in table_rows:
        cells = row.find_elements(By.TAG_NAME, 'span')
        print(cells[column_index].text)

def test_search2(driver):
    column_name = "CPU"
    table_rows = driver.find_elements(By.XPATH, "//div[@role='row']")

#print table headers
    table_headers_obj = driver.find_elements(By.XPATH, "//span[@role='columnheader']")
    table_headers = [i.text for i in table_headers_obj]
    print(*table_headers)

#print number of rows
    print("\nnumber of rows in the table is", len(table_rows), end= '\n\n')

#print column given column name
    time.sleep(3)
    column_index = table_headers.index(column_name)
    for row in table_rows:
        cells = row.find_elements(By.TAG_NAME, 'span' )
        print(cells[column_index].text)
