from selenium.webdriver.common.by import By
from Locators.informationPageLocators import InformationPageLocators

class InformationPage():
    def __init__(self, driver):
        self.driver = driver
        self.textbox_firstname_id = InformationPageLocators.textbox_firstname_id
        self.textbox_lastname_id = InformationPageLocators.textbox_lastname_id
        self.textbox_zip_id = InformationPageLocators.textbox_zip_id
        self.button_cancel_id = InformationPageLocators.button_cancel_id
        self.button_continue_id = InformationPageLocators.button_continue_id
        self.message_error_css = InformationPageLocators.message_error_css

    def enter_firstname(self, firstname):
        self.driver.find_element(By.ID, self.textbox_firstname_id).send_keys(firstname)

    def enter_lastname(self, lastname):
        self.driver.find_element(By.ID, self.textbox_lastname_id).send_keys(lastname)

    def enter_zip(self, zip):
        self.driver.find_element(By.ID, self.textbox_zip_id).send_keys(zip)

    def click_cancel(self):
        self.driver.find_element(By.ID, self.button_cancel_id).click()

    def click_continue(self):
        self.driver.find_element(By.ID, self.button_continue_id).click()

    def error_message_text(self):
        error_msg = self.driver.find_element(By.CSS_SELECTOR, self.message_error_css)
        error_msg_text = error_msg.text
        return error_msg_text



