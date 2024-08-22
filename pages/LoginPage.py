from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class LoginPage(BasePage):
    URL = "https://the-internet.herokuapp.com/login"
    TITLE = "The Internet"
# elements
    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    BUTTON_LOGIN = (By.CLASS_NAME, "radius")
    CONFIRM_LOGOUT = (By.ID, "flash")

# constructor
    def __init__(self, driver):
        super().__init__(driver)

# services
    def open(self):
        self.open_page(self.URL, self.TITLE)
        return self

    def submit_login(self, username, password):
        self.find_element(self.USERNAME).send_keys(username)
        self.find_element(self.PASSWORD).send_keys(password)
        self.click_element(self.BUTTON_LOGIN)

    def valid_login(self, username, password):
        from pages.HomePage import HomePage
        self.submit_login(username, password)
        return HomePage(self.driver)

    def invalid_login(self, username, password):
        self.submit_login(username, password)
        return self

    def get_notification(self):
        return self.find_element(self.CONFIRM_LOGOUT).text
