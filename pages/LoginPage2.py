from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class LoginPage(BasePage):
    URL = "https://the-internet.herokuapp.com/login"
    TITLE = 'The Internet'
    # elements
    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, 'password')
    BUTTON_LOGIN = (By.TAG_NAME, 'button')
    NOTIFICATION_BAR = (By.ID, 'flash')

    # constructor
    def __init__(self, driver):
        super().__init__(driver)
        self.username_input = self.find_element(self.USERNAME)
        self.password_input = self.find_element(self.PASSWORD)
        self.button_login = self.find_element(self.BUTTON_LOGIN)
        self.notification_bar = self.find_element(self.NOTIFICATION_BAR)

    # services
    def open(self):
        self.open_page(self.URL, self.TITLE)
        return self
    # "return self" is needed to later be able to do this
    # user.func1().func2() instead of
    # user.func1() ; user.func2()

    def submit_login(self, username, password):
        self.username_input.send_keys(username)
        self.password_input.send_keys(password)
        self.click_element(self.BUTTON_LOGIN)

    def valid_login(self, username, password):
        from pages.HomePage import HomePage
        self.submit_login(username, password)
        return HomePage(self.driver)

    def invalid_login(self, username, password):
        self.submit_login(username, password)
        return self

    def get_notification(self):
        return self.notification_bar.text
