import unittest
from selenium import webdriver
from pages.loginPage import LoginPage
from elements.globalVariable import GlobalVariable


class Login(unittest.TestCase):

    def setUp(self):
        # You can change the webdriver setting for windows or mac here
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        capabilities = options.to_capabilities()

        self.driver = webdriver.Chrome(GlobalVariable.driver_location, desired_capabilities=capabilities)
        self.driver.get(GlobalVariable.url_link)

    def test_login_invalid_email(self):
        login_page = LoginPage(self.driver)
        login_page.username_text_element = GlobalVariable.invalid_email
        login_page.password_text_element = GlobalVariable.valid_email
        login_page.select_admin_role()
        login_page.click_login_button()

    def test_login_invalid_password(self):
        login_page = LoginPage(self.driver)
        login_page.username_text_element = GlobalVariable.valid_email
        login_page.password_text_element = GlobalVariable.invalid_password
        login_page.select_admin_role()
        login_page.click_login_button()

    def test_login_invalid_role(self):
        login_page = LoginPage(self.driver)
        login_page.username_text_element = GlobalVariable.valid_email
        login_page.password_text_element = GlobalVariable.valid_password
        login_page.select_moderator_role()
        login_page.click_login_button()

    def test_login_valid(self):
        login_page = LoginPage(self.driver)
        login_page.username_text_element = GlobalVariable.valid_email
        login_page.password_text_element = GlobalVariable.valid_password
        login_page.select_admin_role()
        login_page.click_login_button()

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
