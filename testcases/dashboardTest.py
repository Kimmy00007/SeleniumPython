import unittest
from selenium import webdriver
from pages.dashboardPage import DashboardPage
from pages.loginPage import LoginPage
from elements.globalVariable import GlobalVariable


class Dashboard(unittest.TestCase):

    def setUp(self):
        # You can change the webdriver setting for windows or mac here
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        capabilities = options.to_capabilities()

        self.driver = webdriver.Chrome(GlobalVariable.driver_location, desired_capabilities=capabilities)
        self.driver.get(GlobalVariable.url_link)

    def test_click_surveyMenu(self):
        login_page = LoginPage(self.driver)
        dashboard_page = DashboardPage(self.driver)
        login_page.username_text_element = "user_admin_1@snapcart.asia"
        login_page.password_text_element = "123123"
        login_page.select_admin_role()
        login_page.click_login_button()
        dashboard_page.open_survey_menu()

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
