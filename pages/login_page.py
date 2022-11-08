from selenium.webdriver.common.by import By

from pages.basepage import BasePage


class LoginPage(BasePage):
    username = (By.NAME, "username")
    password = (By.NAME, "password")
    loginButton = (By.TAG_NAME, "button")
    forgotPasswordLink = (By.XPATH, "//p[contains(@class,'orangehrm-login-forgot-header')]")

    def __init__(self, driver):
        super().__init__(driver)

    def get_login_page_title(self, title):
        return self.get_title(title)

    def is_Forgot_Password_Link_exist(self):
        return self.is_visible(self.forgotPasswordLink)

    def login(self, username, password):
        self.do_send_keys(self.username, username)
        self.do_send_keys(self.password, password)
        self.do_click(self.loginButton)


