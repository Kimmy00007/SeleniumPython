from selenium.webdriver.common.by import By


class DashboardPageLocators(object):
    CMS_menu = (By.XPATH, '/html/body/div[3]/div[1]/div/ul/li[10]/a')
    surveyList_CMS_menu = (By.XPATH, '/html/body/div[3]/div[1]/div/ul/li[10]/ul/li[4]/a')

