import allure
from selenium.webdriver.common.by import By

from conftest import click_element


@allure.feature('Login functionality')
@allure.story('Valid credentials')
@allure.severity(allure.severity_level.CRITICAL)
def test_valid_login(driver):
    with allure.step('Open login page'):
        driver.get("https://the-internet.herokuapp.com/login")
    with allure.step('enter valid credentials'):
        driver.find_element(By.ID, 'username').send_keys('tomsmith')
        driver.find_element(By.ID, 'password').send_keys('SuperSecretPassword!')
    with allure.step('click "login" button'):
        click_element(driver, (By.TAG_NAME, 'button'))
    with allure.step('verify login success'):
        confirm_login = driver.find_element(By.ID, 'flash')
        assert 'You logged into' in confirm_login.text
        allure.attach('login successful', name = 'Success',
                      attachment_type=allure.attachment_type.TEXT)
