from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class HomePage(BasePage):
    TITLE = "The Internet"
# elements
    BUTTON_LOGOUT = (By.CSS_SELECTOR, '.button.secondary.radius')
    NOTIFICATION_BAR = (By.ID, 'flash')

# constructor
    def __init__(self, driver):
        super().__init__(driver)
        assert self.driver.title == self.TITLE
        self.button_logout = self.find_element(self.BUTTON_LOGOUT)
        self.notification_bar = self.find_element(self.NOTIFICATION_BAR)

# services
    def logout(self):
        from pages.LoginPage2 import LoginPage
        self.click_element(self.BUTTON_LOGOUT)
        return LoginPage(self.driver)

    def get_notification(self):
        return self.notification_bar.text

