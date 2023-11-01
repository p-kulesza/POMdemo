from selenium.webdriver.common.by import By
from Locators.loginPageLocators import LoginPageLocators


class LoginPage():
    def __init__(self,driver):
        self.driver = driver
        self.textbox_login_id = LoginPageLocators.texbox_login_id
        self.textbox_password_id = LoginPageLocators.textbox_password_id
        self.button_login_id = LoginPageLocators.button_login_id
        self.alert_error_xpath = LoginPageLocators.alert_error_xpath
        self.logo_css = LoginPageLocators.logo_css

    def enter_login(self, login):
        self.driver.find_element(By.ID, self.textbox_login_id).clear()
        self.driver.find_element(By.ID, self.textbox_login_id).send_keys(login)

    def enter_password(self, password):
        self.driver.find_element(By.ID, self.textbox_password_id).clear()
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.ID, self.button_login_id).click()

    def error_text(self):
        alert = self.driver.find_element(By.XPATH, self.alert_error_xpath)
        return alert.text

    def logo_text(self):
        logo = self.driver.find_element(By.CSS_SELECTOR, self.logo_css)
        logo_text = logo.text
        return logo_text
