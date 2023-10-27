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
        options = webdriver.FirefoxOptions()
        options.add_argument("--headless")
        cls.driver = webdriver.Firefox(service=service_obj, options=options)
        cls.driver.implicitly_wait(5)
        print("SetUp complete.")

    def test_login_valid(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        loginpage = LoginPage(driver)
        homepage = HomePage(driver)
        loginpage.enter_login("standard_user")
        loginpage.enter_password("secret_sauce")
        loginpage.click_login()
        homepage.app_logo_presence()

    def test_locked_user(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        loginpage = LoginPage(driver)
        loginpage.enter_login("locked_out_user")
        loginpage.enter_password("secret_sauce")
        loginpage.click_login()
        self.assertEqual(loginpage.error_text(), "Epic sadface: Sorry, this user has been locked out.")

    def test_login_invalid_username(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        loginpage = LoginPage(driver)
        loginpage.enter_login("standar_user")
        loginpage.enter_password("secret_sauce")
        loginpage.click_login()
        self.assertEqual(loginpage.error_text(), "Epic sadface: Username and password do not match any user in this service")

    def test_login_invalid_password(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        loginpage = LoginPage(driver)
        loginpage.enter_login("standard_user")
        loginpage.enter_password("secre_sauce")
        loginpage.click_login()
        self.assertEqual(loginpage.error_text(), "Epic sadface: Username and password do not match any user in this service")

    def test_login_invalid_empty_creds(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        loginpage = LoginPage(driver)
        loginpage.click_login()
        self.assertEqual(loginpage.error_text(), "Epic sadface: Username is required")

    def test_login_invalid_empty_username(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        loginpage = LoginPage(driver)
        loginpage.enter_password("secret_sauce")
        loginpage.click_login()
        self.assertEqual(loginpage.error_text(), "Epic sadface: Username is required")

    def test_login_invalid_empty_password(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        loginpage = LoginPage(driver)
        loginpage.enter_login("standard_user")
        loginpage.click_login()
        self.assertEqual(loginpage.error_text(), "Epic sadface: Password is required")

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("TearDown complete.")


