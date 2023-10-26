from selenium.webdriver.common.by import By


class OverviewPage():
    def __init__(self, driver):
        self.driver = driver
        self.button_cancel_id = "cancel"
        self.button_finish_id = "finish"
        self.button_remove_css = ".btn.btn_secondary.btn_small.cart_button"
        self.overview_container_css = ".checkout_summary_container"
        self.item_name_css = ".inventory_item_name"
        #whole payment info into text!!!
        #product name == product in cart

    def click_cancel(self):
        self.driver.find_element(By.ID, self.button_cancel_id).click()

    def click_finish(self):
        self.driver.find_element(By.ID, self.button_finish_id).click()

    def print_summary_info(self):
        summary = self.driver.find_element(By.CSS_SELECTOR, self.overview_container_css)
        print(summary.text)

    def get_item_name_text(self):
        item_names = self.driver.find_elements(By.CSS_SELECTOR, self.item_name_css)
        itemList = []
        for item_name in item_names:
            item_text = item_name.text
            itemList.append(item_text)
        return itemList
