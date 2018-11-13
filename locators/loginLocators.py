from selenium.webdriver.common.by import By


class LoginPageLocators(object):
    admin_option = (By.XPATH, '//*[@id="type"]/option[2]')
    moderator_option = (By.XPATH, '//*[@id="type"]/option[1]')
    login_button = (By.XPATH, '/html/body/div[2]/form/div[4]/button')
    error_notif = (By.XPATH, '/html/body/div[2]/form/div[1]/span')
