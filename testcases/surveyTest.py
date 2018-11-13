import unittest
import datetime
from selenium import webdriver
from pages.dashboardPage import DashboardPage
from pages.loginPage import LoginPage
from elements.globalVariable import GlobalVariable
from pages.surveyPage import SurveyPage


class Survey(unittest.TestCase):

    def setUp(self):
        # You can change the webdriver setting for windows or mac here
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        capabilities = options.to_capabilities()

        self.driver = webdriver.Chrome(GlobalVariable.driver_location, desired_capabilities=capabilities)
        self.driver.get(GlobalVariable.url_link)
        self.today_date = datetime.date.today().strftime('%d/%m/%Y %H:%m')

    def test_login(self):
        login_page = LoginPage(self.driver)
        login_page.username_text_element = GlobalVariable.valid_email
        login_page.password_text_element = GlobalVariable.valid_password
        login_page.select_admin_role()
        login_page.click_login_button()

    def test_open_surveyMenu(self):
        self.test_login()
        dashboard_page = DashboardPage(self.driver)
        dashboard_page.open_survey_menu()

    def test_open_createNewSurvey(self):
        self.test_open_surveyMenu()
        survey_page = SurveyPage(self.driver)
        survey_page.create_new_survey()

    def test_create_newSurvey(self):
        self.test_open_createNewSurvey()
        survey_page = SurveyPage(self.driver)
        survey_page.field_name_en = "Automation Survey ", self.today_date
        survey_page.field_name_id = "Survey Otomasi", self.today_date
        survey_page.field_desc_en = "Automation Description", self.today_date
        survey_page.field_desc_id = "Deskripsi Otomasi", self.today_date

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
