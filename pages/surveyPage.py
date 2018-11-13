from locators.surveyLocators import SurveyPageLocators
from elements.globalVariable import GlobalVariable
from elements.baseElement import BasePageElementByXpath


class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""
    def __init__(self, driver):
        self.driver = driver


class FieldNameEN(BasePageElementByXpath):
    locator = '//*[@id="survey_name_en"]'


class FieldNameID(BasePageElementByXpath):
    locator = '//*[@id="survey_name_id"]'


class FieldDescEN(BasePageElementByXpath):
    locator = '//*[@id="survey_description_en"]'


class FieldDescID(BasePageElementByXpath):
    locator = '//*[@id="survey_description_id"]'


class FieldQuantity(BasePageElementByXpath):
    locator = '//*[@id="survey_add_quantity"]'


class SurveyPage(BasePage):
    field_name_en = FieldNameEN()
    field_name_id = FieldNameID()
    field_desc_en = FieldDescEN()
    field_desc_id = FieldDescID()
    field_quantity = FieldQuantity()

    def create_new_survey(self):
        element = self.driver.find_element(*SurveyPageLocators.button_createNew_survey)
        element.click()
