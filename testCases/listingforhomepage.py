from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.select import Select
import unittest

from Pages.homePage import HomePage
from Pages.loginPage import LoginPage
class PróbnyTest(unittest.TestCase):
    def test_1(self):
        service_obj = Service("C:\\Users\\Admin\\Desktop\\geckodriver-v0.33.0-win64\\geckodriver.exe")
        driver = webdriver.Firefox(service=service_obj)
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.get("https://www.saucedemo.com/")
        print(driver.title)
        if driver.title == "Swag Labs":
            print("OK")
        loginpage = LoginPage(driver)
        homepage = HomePage(driver)
        loginpage.enter_login("standard_user")
        loginpage.enter_password("secret_sauce")
        loginpage.click_login()
        div_elements = driver.find_elements(By.CSS_SELECTOR, ".inventory_item_name")

        ActualList = []

        for div_element in div_elements:
            div_text = div_element.text
            print(div_text)
            ActualList.append(div_text)

        ActualList.sort()
        print(ActualList)
        ExpectedList = ['Sauce Labs Backpack', 'Sauce Labs Bike Light', 'Sauce Labs Bolt T-Shirt', 'Sauce Labs Fleece Jacket', 'Sauce Labs Onesie', 'Test.allTheThings() T-Shirt (Red)']
        self.assertEqual(ActualList, ExpectedList)




