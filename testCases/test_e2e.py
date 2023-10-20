import unittest
from selenium.webdriver.firefox.service import Service
from selenium import webdriver

from Pages.homePage import HomePage
from Pages.loginPage import LoginPage


class end2end(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        service_obj = Service("C:\\Users\\user\\Desktop\\geckodriver\\geckodriver.exe")
        cls.driver = webdriver.Firefox(service=service_obj)
        cls.driver.maximize_window()

    def test_login_valid_plus_reset(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        loginpage = LoginPage(driver)
        loginpage.enter_login("standard_user")
        loginpage.enter_password("secret_sauce")
        loginpage.click_login()

        homepage = HomePage(driver)
        homepage.click_menu()
        homepage.click_reset()