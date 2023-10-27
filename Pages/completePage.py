from selenium.webdriver.common.by import By
from Locators.completePageLocators import CompletedPageLocators

class CompletePage():
    def __init__(self, driver):
        self.driver = driver
        self.text_complete_header_css = CompletedPageLocators.text_complete_header_css
        self.button_back_id = CompletedPageLocators.button_back_id

    def complete_header_presence(self):
        self.driver.find_element(By.CSS_SELECTOR, self.text_complete_header_css)

    def click_back_home(self):
        self.driver.find_element(By.ID, self.button_back_id).click()
