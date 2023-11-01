from selenium.webdriver.common.by import By
from Locators.overviewPageLocators import OverviewPageLocators

class OverviewPage():
    def __init__(self, driver):
        self.driver = driver
        self.button_cancel_id = OverviewPageLocators.button_cancel_id
        self.button_finish_id = OverviewPageLocators.button_finish_id
        self.button_remove_xpath = OverviewPageLocators.button_remove_xpath
        self.overview_container_css = OverviewPageLocators.overview_container_css
        self.item_name_css = OverviewPageLocators.item_name_css

    def click_cancel(self):
        self.driver.find_element(By.ID, self.button_cancel_id).click()

    def click_finish(self):
        self.driver.find_element(By.ID, self.button_finish_id).click()

    def summary_info(self):
        summary = self.driver.find_element(By.CSS_SELECTOR, self.overview_container_css)
        return summary.text #return summary.text?


    def get_item_name_text(self):
        item_names = self.driver.find_elements(By.CSS_SELECTOR, self.item_name_css)
        itemList = []
        for item_name in item_names:
            item_text = item_name.text
            itemList.append(item_text)
        return itemList


