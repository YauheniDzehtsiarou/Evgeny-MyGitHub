import time

import pytest
from selenium.webdriver.common.by import By


@pytest.fixture(autouse=True)
def setup(driver):
    driver.get('https://the-internet.herokuapp.com/tables')

def test_tables(driver):
    column_number = 4
    table_rows = driver.find_elements(By.XPATH, "//table[2]/tbody/tr")
    time.sleep(2)
    number_of_rows = len(table_rows)
    print("\nnumber of rows is",number_of_rows)

    for row in table_rows:
        print(row.text)

#1
    print("\noption1")
    for row in table_rows:
        print(row.text.split()[column_number-1])
    time.sleep(10)

#2
    print("\noption2")
    for i in range(1, number_of_rows+1):
        cell_xpath = f"//table[2]/tbody[1]/tr[{i}]/td[{column_number}]"
        print(driver.find_element(By.XPATH,cell_xpath).text)

#3
    print("\noption3")
    dues = driver.find_elements(By.CLASS_NAME, "dues")
    for i in range(1, number_of_rows+1):
        print(dues[i].text)

#4
    print("\noption4")
    for row in table_rows:
        print(row.find_element(By.CLASS_NAME, "dues").text)

