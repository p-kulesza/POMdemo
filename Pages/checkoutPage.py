from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec


class CheckoutPage():
    def __init__(self, driver):
        self.driver = driver
        self.button_checkout_css = "#checkout"
        self.button_continue_shopping_css = "#continue-shopping"
        self.button_menu_xpath = "//div[@class='bm-burger-button']"
        self.button_remove_xpath = "//button[contains(text(),'Remove')]"
        self.inventory_item_name_css = ".inventory_item_name"
        self.yourcart_text_presence_xpath = "//span[contains(text(),'Your Cart')]"
        self.item_description_css = ".inventory_item_desc"

    def click_checkout(self):
        self.driver.find_element(By.CSS_SELECTOR, self.button_checkout_css).click()

    def click_continue_shopping(self):
        self.driver.find_element(By.CSS_SELECTOR, self.button_continue_shopping_css).click()

    def click_menu_button(self):
        self.driver.find_element(By.XPATH, self.button_menu_xpath).click()

    def list_number_of_items(self):
        list = self.driver.find_elements(By.CSS_SELECTOR, self.inventory_item_name_css)
        return len(list)

    def item_description(self):
        self.driver.find_element(By.CSS_SELECTOR, self.item_description_css)

    def delete_item(self):
        self.driver.find_element(By.XPATH, self.button_remove_xpath).click()