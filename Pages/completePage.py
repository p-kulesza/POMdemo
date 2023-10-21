from selenium.webdriver.common.by import By


class CompletePage():
    def __init__(self, driver):
        self.driver = driver
        self.text_complete_header_css = ".complete-header"
        self.button_back_css = ".btn btn_primary btn_small"

    def complete_header_presence(self):
        self.driver.find_element(By.CSS_SELECTOR, self.text_complete_header_css)

    def click_back_home(self):
        self.driver.find_element(By.CSS_SELECTOR, self.button_back_css).click()
