import unittest

from selenium import webdriver
from selenium.webdriver.firefox.service import Service

from Pages.checkoutPage import CheckoutPage
from Pages.homePage import HomePage
from Pages.informationPage import InformationPage
from Pages.loginPage import LoginPage


class InformationPageTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        service_obj = Service("C:\\Users\\Admin\\Desktop\\geckodriver-v0.33.0-win64\\geckodriver.exe")
        options = webdriver.FirefoxOptions()
        options.add_argument("--headless")
        cls.driver = webdriver.Firefox(service=service_obj, options=options)
        cls.driver.implicitly_wait(5)
        print("SetUp complete.")

    def login_and_checkout_step(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        loginpage = LoginPage(driver)
        homepage = HomePage(driver)
        checkout = CheckoutPage(driver)
        loginpage.enter_login("standard_user")
        loginpage.enter_password("secret_sauce")
        loginpage.click_login()
        homepage.click_addtocart()
        homepage.click_checkout()
        checkout.click_checkout()

    def test_empty_information(self):
        self.login_and_checkout_step()
        driver = self.driver
        information = InformationPage(driver)
        information.click_continue()
        information.error_message_presence()

    def test_no_firstname_information(self):
        self.login_and_checkout_step()
        driver = self.driver
        information = InformationPage(driver)
        information.enter_lastname("Kowalski")
        information.enter_zip("11-111")
        information.click_continue()
        information.error_message_presence()

    def test_no_lastname_information(self):
        self.login_and_checkout_step()
        driver = self.driver
        information = InformationPage(driver)
        information.enter_firstname("Piotr")
        information.enter_zip("11-111")
        information.click_continue()
        information.error_message_presence()

    def test_no_zipcode_information(self):
        self.login_and_checkout_step()
        driver = self.driver
        information = InformationPage(driver)
        information.enter_firstname("Piotr")
        information.enter_lastname("Kowalski")
        information.click_continue()
        information.error_message_presence()

    def test_valid_information_continue(self):
        self.login_and_checkout_step()
        driver = self.driver
        information = InformationPage(driver)
        information.enter_firstname("Piotr")
        information.enter_lastname("Kowalski")
        information.enter_zip("66-666")
        information.click_continue()


    def test_valid_information_cancel(self):
        self.login_and_checkout_step()
        driver = self.driver
        information = InformationPage(driver)
        checkout = CheckoutPage(driver)
        information.enter_firstname("Piotr")
        information.enter_lastname("Kowalski")
        information.enter_zip("11-111")
        information.click_cancel()
        checkout.item_description() #successfully came back to checkout page

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("TearDown complete.")