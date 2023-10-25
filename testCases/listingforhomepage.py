from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.select import Select
import unittest

from Pages.checkoutPage import CheckoutPage
from Pages.homePage import HomePage
from Pages.informationPage import InformationPage
from Pages.loginPage import LoginPage
from Pages.overviewPage import OverviewPage


class PróbnyTest(unittest.TestCase):
    def __init__(self, methodName: str = ...):
        super().__init__(methodName)

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
        homepage.select_product_sort_visible_text("Price (low to high)")
        div_elements = driver.find_elements(By.CSS_SELECTOR, homepage.price_css)
        actualList = []
        for div_element in div_elements:
            div_text = div_element.text
            actualList.append(div_text)
        print(actualList)

    def test_2(self):
        service_obj = Service("C:\\Users\\Admin\\Desktop\\geckodriver-v0.33.0-win64\\geckodriver.exe")
        driver = webdriver.Firefox(service=service_obj)
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.get("https://www.saucedemo.com/")
        loginpage = LoginPage(driver)
        homepage = HomePage(driver)
        checkout = CheckoutPage(driver)
        information = InformationPage(driver)
        overview = OverviewPage(driver)
        loginpage.enter_login("standard_user")
        loginpage.enter_password("secret_sauce")
        loginpage.click_login()
        homepage.click_addtocart()
        homepage.click_addtocart()
        homepage.click_checkout()
        checkout.click_checkout()
        information.enter_zip("11111")
        information.enter_firstname("111")
        information.enter_lastname("1111")
        information.click_continue()
        overview.print_summary_info()




