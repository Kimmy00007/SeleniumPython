from elements.globalVariable import GlobalVariable


class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver


class DashboardPage(BasePage):

    def open_survey_menu(self):
        self.driver.get(GlobalVariable.url_link + "/cms/surveys/")
