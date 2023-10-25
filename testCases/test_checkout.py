import unittest

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.firefox.service import Service

from Pages.checkoutPage import CheckoutPage
from Pages.homePage import HomePage
from Pages.loginPage import LoginPage


class CheckoutPageTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        service_obj = Service("C:\\Users\\Admin\\Desktop\\geckodriver-v0.33.0-win64\\geckodriver.exe")
        options = webdriver.FirefoxOptions()
        options.add_argument("--headless")
        cls.driver = webdriver.Firefox(service=service_obj, options=options)
        cls.driver.implicitly_wait(5)
        print("SetUp complete.")

    def login_step(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        loginpage = LoginPage(driver)
        loginpage.enter_login("standard_user")
        loginpage.enter_password("secret_sauce")
        loginpage.click_login()
        print("Successfully logged in")

    def test_empty_checkout(self):
        driver = self.driver
        checkout = CheckoutPage(driver)
        homepage = HomePage(driver)
        self.login_step()
        homepage.click_checkout()
        checkout.click_checkout()
        checkout.yourcart_presence_assertion()

        #add assertion

    def test_reset_checkout(self):
        driver = self.driver
        checkout = CheckoutPage(driver)
        homepage = HomePage(driver)
        self.login_step()
        homepage.click_addtocart()
        homepage.click_checkout()
        checkout.click_menu_button()
        homepage.click_reset()
        #reset does nothing on this stage for some reason :(

    def test_item_description_presence(self):
        driver = self.driver
        checkout = CheckoutPage(driver)
        homepage = HomePage(driver)
        self.login_step()
        homepage.click_addtocart()
        homepage.click_checkout()
        #checkout.item_description().is_displayed()
        #NoSuchElementException

    def test_multiple_items(self):
        driver = self.driver
        checkout = CheckoutPage(driver)
        homepage = HomePage(driver)
        self.login_step()
        homepage.click_addtocart()
        homepage.click_addtocart()

    #add items + check if price is correct (go to overview and check .summary_subtotal_label)

    def test_multiple_items_delete_one(self):
        driver = self.driver
        checkout = CheckoutPage(driver)
        homepage = HomePage(driver)
        self.login_step()
    #add items + check if price is correct + delete one + check if one is left

    def test_mulitple_items_delete_all(self):
        driver = self.driver
        checkout = CheckoutPage(driver)
        homepage = HomePage(driver)
        self.login_step()

    def test_a(self):
        driver = self.driver
        checkout = CheckoutPage(driver)
        homepage = HomePage(driver)
        self.login_step()


    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("TearDown complete.")