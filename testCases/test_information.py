import unittest

from selenium import webdriver
from selenium.webdriver.firefox.service import Service

from Pages.checkoutPage import CheckoutPage
from Pages.homePage import HomePage
from Pages.informationPage import InformationPage
from Pages.loginPage import LoginPage
from Pages.overviewPage import OverviewPage


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

    def reset_page(self):
        driver = self.driver #necessary step, source page doesn't delete items after closing.
        checkout = CheckoutPage(driver)
        homepage = HomePage(driver)
        checkout.click_menu_button()
        homepage.click_reset()

    def test_empty_information(self):
        self.login_and_checkout_step()
        driver = self.driver
        information = InformationPage(driver)
        information.click_continue()
        assert "Error: First Name is required" in information.error_message_text()
        self.reset_page()

    def test_no_firstname_information(self):
        self.login_and_checkout_step()
        driver = self.driver
        information = InformationPage(driver)
        information.enter_lastname("Kowalski")
        information.enter_zip("11-111")
        information.click_continue()
        assert "Error: First Name is required" in information.error_message_text()
        self.reset_page()

    def test_no_lastname_information(self):
        self.login_and_checkout_step()
        driver = self.driver
        information = InformationPage(driver)
        information.enter_firstname("Piotr")
        information.enter_zip("11-111")
        information.click_continue()
        assert "Error: Last Name is required" in information.error_message_text()
        self.reset_page()

    def test_no_zipcode_information(self):
        self.login_and_checkout_step()
        driver = self.driver
        information = InformationPage(driver)
        information.enter_firstname("Piotr")
        information.enter_lastname("Kowalski")
        information.click_continue()
        assert "Error: Postal Code is required" in information.error_message_text()
        self.reset_page()

    def test_valid_information_continue(self):
        self.login_and_checkout_step()
        driver = self.driver
        information = InformationPage(driver)
        overview = OverviewPage(driver)
        information.enter_firstname("Piotr")
        information.enter_lastname("Kowalski")
        information.enter_zip("66-666")
        information.click_continue()
        assert "Finish" in overview.summary_info() #assertion - change of url
        self.reset_page()

    def test_valid_information_cancel(self):
        self.login_and_checkout_step()
        driver = self.driver
        information = InformationPage(driver)
        checkout = CheckoutPage(driver)
        information.enter_firstname("Piotr")
        information.enter_lastname("Kowalski")
        information.enter_zip("11-111")
        information.click_cancel()
        self.assertEqual(len(checkout.item_description()), 1) #successfully came back to checkout page
        self.reset_page()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("TearDown complete.")