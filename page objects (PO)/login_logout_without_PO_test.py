import pytest
from selenium.webdriver.common.by import By

from conftest import click_element


@pytest.fixture(autouse= True)
def setup(driver):
    driver.get("https://the-internet.herokuapp.com/login")

def test_valid_login(driver):
    driver.find_element(By.ID, 'username').send_keys('tomsmith')
    driver.find_element(By.ID, 'password').send_keys('SuperSecretPassword!')
    #driver.find_element(By.TAG_NAME, 'button').click()
    click_element(driver, (By.TAG_NAME, 'button'))
    confirm_login = driver.find_element(By.ID, 'flash')
    assert 'You logged into' in confirm_login.text

    click_element(driver, (By.CSS_SELECTOR, '.button.secondary.radius'))
    confirm_logout = driver.find_element(By.ID, 'flash')
    assert 'You logged out' in confirm_logout.text