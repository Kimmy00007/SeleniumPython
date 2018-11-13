from elements.baseElement import BasePageElementByName
from locators.loginLocators import LoginPageLocators


class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver


class UsernameTextElement(BasePageElementByName):
    locator = '_username'


class PasswordTextElement(BasePageElementByName):
    locator = '_password'


class LoginPage(BasePage):
    username_text_element = UsernameTextElement()
    password_text_element = PasswordTextElement()

    def select_admin_role(self):
        element = self.driver.find_element(*LoginPageLocators.admin_option)
        element.click()

    def select_moderator_role(self):
        element = self.driver.find_element(*LoginPageLocators.moderator_option)
        element.click()

    def click_login_button(self):
        element = self.driver.find_element(*LoginPageLocators.login_button)
        element.click()

