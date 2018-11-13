from selenium.webdriver.common.by import By


class SurveyPageLocators(object):
    button_createNew_survey = (By.XPATH, '//div/div/div/div/a')


class CreateNewSurveyPageLocators(object):
    status_Draft = (By.XPATH, '//*[@id="survey_status"]/option[1]')
    status_Pending = (By.XPATH, '//*[@id="survey_status"]/option[2]')
    status_Active = (By.XPATH, '//*[@id="survey_status"]/option[3]')
    status_Expired = (By.XPATH, '//*[@id="survey_status"]/option[4]')
    field_quantity = (By.XPATH, '')
