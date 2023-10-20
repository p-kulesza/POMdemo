import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium import webdriver
from Pages.loginPage import LoginPage
from Pages.homePage import HomePage

class LoginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        service_obj = Service("C:\\Users\\Admin\\Desktop\\geckodriver-v0.33.0-win64\\geckodriver.exe")
        cls.driver = webdriver.Firefox(service=service_obj)
        cls.driver.maximize_window()

    def test_login_valid_plus_logout(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        loginpage = LoginPage(driver)
        loginpage.enter_login("standard_user")
        loginpage.enter_password("secret_sauce")
        loginpage.click_login()

        homepage = HomePage(driver)
        homepage.click_menu()
        homepage.click_reset()

    def test_login_invalid_plus_logout(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        loginpage = LoginPage(driver)
        loginpage.enter_login("standar_user")
        loginpage.enter_password("secret_sauce")
        loginpage.click_login()
        loginpage.error_text_presence()



    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("TearDown complete.")


