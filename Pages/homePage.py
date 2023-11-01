from selenium.webdriver.common.by import By
from Locators.homePageLocators import HomePageLocators

from selenium.webdriver.support.select import Select



class HomePage():
    def __init__(self,driver):
        self.driver = driver
        self.button_menu_xpath = HomePageLocators.button_menu_xpath
        self.button_reset_id = HomePageLocators.button_reset_id
        self.button_allitems_id = HomePageLocators.button_allitems_id
        self.button_about_id = HomePageLocators.button_about_id
        self.button_logout_id = HomePageLocators.button_logout_id
        self.app_logo_css = HomePageLocators.app_logo_css
        self.button_checkout_css = HomePageLocators.button_checkout_css
        self.button_sort_css = HomePageLocators.button_sort_css
        self.button_addtocart_xpath = HomePageLocators.button_addtocart_xpath
        self.inventory_item_css = HomePageLocators.inventory_item_css
        self.price_css = HomePageLocators.price_css

    def click_menu(self):
        self.driver.find_element(By.XPATH, self.button_menu_xpath).click()

    def menu_correctnes(self):
        self.driver.find_element(By. ID, self.button_allitems_id)
        self.driver.find_element(By.ID, self.button_about_id)
        self.driver.find_element(By.ID, self.button_logout_id)
        self.driver.find_element(By.ID, self.button_reset_id)
        print("Menu present, all options correct.")

    def click_allitems(self):
        self.driver.find_element(By.ID, self.button_allitems_id).click()
    def click_reset(self):
        self.driver.find_element(By.ID, self.button_reset_id).click()
    def click_about(self):
        self.driver.find_element(By.ID, self.button_about_id).click()
    def click_logout(self):
        self.driver.find_element(By.ID, self.button_logout_id).click()
    def app_logo_presence(self):
        logo = self.driver.find_element(By.CSS_SELECTOR, self.app_logo_css)
        logo_text = logo.text
        return logo_text
    def click_checkout(self):
        self.driver.find_element(By.CSS_SELECTOR, self.button_checkout_css).click()
    def click_addtocart(self):
        self.driver.find_element(By.XPATH, self.button_addtocart_xpath).click()
    def number_of_items(self):
        list = self.driver.find_elements(By.CSS_SELECTOR, self.inventory_item_css)
        print(len(list))

    def list_products(self):
        div_elements = self.driver.find_elements(By.CSS_SELECTOR, self.inventory_item_css)
        actualList = []
        for div_element in div_elements:
            div_text = div_element.text
            actualList.append(div_text)
        return actualList

    def select_product_sort_visible_text(self, visible_text):
        from selenium.webdriver.support.select import Select
        sel = Select(self.driver.find_element(By.CSS_SELECTOR, self.button_sort_css))
        sel.select_by_visible_text(visible_text)

    def list_price(self):
        div_elements = self.driver.find_elements(By.CSS_SELECTOR, self.price_css)
        actualList = []
        for div_element in div_elements:
            div_text = div_element.text
            actualList.append(div_text)
        return actualList