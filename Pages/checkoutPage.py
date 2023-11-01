from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from Locators.checkoutPageLocators import CheckoutPageLocators


class CheckoutPage():
    def __init__(self, driver):
        self.driver = driver
        self.button_checkout_css = CheckoutPageLocators.button_checkout_css
        self.button_continue_shopping_css = CheckoutPageLocators.button_continue_shopping_css
        self.button_menu_xpath = CheckoutPageLocators.button_menu_xpath
        self.button_remove_xpath = CheckoutPageLocators.button_remove_xpath
        self.inventory_item_name_css = CheckoutPageLocators.inventory_item_name_css
        self.yourcart_text_presence_xpath = CheckoutPageLocators.yourcart_text_presence_xpath
        self.item_description_css = CheckoutPageLocators.item_description_css

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
        desc_list = []
        descriptions = self.driver.find_elements(By.CSS_SELECTOR, self.item_description_css)
        for description in descriptions:
            description_text = description.text
            desc_list.append(description_text)
        return desc_list

    def item_name_text(self):
        item_names = []
        items = self.driver.find_elements(By.CSS_SELECTOR, ".inventory_item_name")
        for item in items:
            item_text = item.text
            item_names.append(item_text)
        return item_names

    def delete_item(self):
        self.driver.find_element(By.XPATH, self.button_remove_xpath).click()