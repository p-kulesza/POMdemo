from selenium.webdriver.common.by import By


class OverviewPage():
    def __init__(self, driver):
        self.driver = driver
        self.button_cancel_id = "cancel"
        self.button_finish_id = "finish"
        self.overview_container_css = ".checkout_summary_container"
        #whole payment info into text!!!
        #product name == product in cart

    def click_cancel(self):
        self.driver.find_element(By.ID, self.button_cancel_id).click()

    def click_finish(self):
        self.driver.find_element(By.ID, self.button_finish_id).click()

    def print_summary_info(self):
        summary = self.driver.find_element(By.CSS_SELECTOR, self.overview_container_css)
        print(summary.text)

