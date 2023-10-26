from selenium.webdriver.common.by import By


class CompletePage():
    def __init__(self, driver):
        self.driver = driver
        self.text_complete_header_css = ".complete-header"
        self.button_back_id = "back-to-products"

    def complete_header_presence(self):
        self.driver.find_element(By.CSS_SELECTOR, self.text_complete_header_css)

    def click_back_home(self):
        self.driver.find_element(By.ID, self.button_back_id).click()
