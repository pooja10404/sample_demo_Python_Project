import pytest

from config.config import TestData
from pages.login_page import LoginPage
from test.test_base import baseTest


class Test_Login(baseTest):

    def test_forgot_link_visible(self):
        self.loginPage = LoginPage(self.driver)
        flag = self.loginPage.forgotPasswordLink
        assert flag

    def test_login_page_title(self):
        self.loginPage = LoginPage(self.driver)
        title = self.loginPage.get_title(TestData.login_Page_title)
        assert title == TestData.login_Page_title

    def test_login(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.login(TestData.username, TestData.password)
