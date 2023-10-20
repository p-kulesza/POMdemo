from selenium.webdriver.common.by import By


class InformationPage():
    def __init__(self, driver):
        self.driver = driver
        self.textbox_firstname_id = "first-name"
        self.textbox_lastname_id = "last-name"
        self.textbox_zip_id = "postal-code"
        self.button_cancel_id = "cancel"
        self.button_continue_id = "continue"
        self.message_error_css = ".error-message-container.error"

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

    def error_message_presence(self):
        self.driver.find_element(By.CSS_SELECTOR, self.message_error_css)



