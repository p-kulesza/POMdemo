
import unittest

from selenium import webdriver
from selenium.webdriver.firefox.service import Service

from Pages.checkoutPage import CheckoutPage
from Pages.homePage import HomePage
from Pages.informationPage import InformationPage
from Pages.loginPage import LoginPage
from Pages.overviewPage import OverviewPage


class OverviewPageTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        service_obj = Service("C:\\Users\\Admin\\Desktop\\geckodriver-v0.33.0-win64\\geckodriver.exe")
        options = webdriver.FirefoxOptions()
        options.add_argument("--headless")
        cls.driver = webdriver.Firefox(service=service_obj, options=options)
        cls.driver.implicitly_wait(5)
        print("SetUp complete.")

    def login_and_checkout_and_info_emtpy_step(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        loginpage = LoginPage(driver)
        homepage = HomePage(driver)
        checkout = CheckoutPage(driver)
        information = InformationPage(driver)
        loginpage.enter_login("standard_user")
        loginpage.enter_password("secret_sauce")
        loginpage.click_login()
        homepage.click_checkout()
        checkout.click_checkout()
        information.enter_firstname("Piotr")
        information.enter_lastname("Kowalski")
        information.enter_zip("11-111")
        information.click_continue()

    def login_checkout_and_info_w_items_step(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        loginpage = LoginPage(driver)
        homepage = HomePage(driver)
        checkout = CheckoutPage(driver)
        information = InformationPage(driver)
        loginpage.enter_login("standard_user")
        loginpage.enter_password("secret_sauce")
        loginpage.click_login()
        homepage.click_addtocart()
        homepage.click_addtocart()
        homepage.click_checkout()
        checkout.click_checkout()
        information.enter_firstname("Piotr")
        information.enter_lastname("Kowalski")
        information.enter_zip("11-111")
        information.click_continue()

    def reset_page(self):
        driver = self.driver #necessary step, source page doesn't delete items after closing.
        checkout = CheckoutPage(driver)
        homepage = HomePage(driver)
        checkout.click_menu_button()
        homepage.click_reset()

    def test_presence_of_payment_info_in_summary(self):
        driver = self.driver
        overview = OverviewPage(driver)
        self.login_checkout_and_info_w_items_step()
        assert "Payment Information" in overview.summary_info()
        self.reset_page()

    def test_presence_of_shipping_info_in_summary(self):
        driver = self.driver
        overview = OverviewPage(driver)
        self.login_checkout_and_info_w_items_step()
        assert "Shipping Information" in overview.summary_info()
        self.reset_page()

    def test_presence_of_price_total_info_in_summary(self):
        driver = self.driver
        overview = OverviewPage(driver)
        self.login_checkout_and_info_w_items_step()
        assert "Price Total" in overview.summary_info()
        self.reset_page()

    def test_summary_info_text(self):
        driver = self.driver
        self.login_checkout_and_info_w_items_step()
        overview = OverviewPage(driver)
        print("Summary info data: " + overview.summary_info())
        self.reset_page()

    def test_summary_info_empty_chart_text(self):
        driver = self.driver
        self.login_and_checkout_and_info_emtpy_step()
        overview = OverviewPage(driver)
        print(overview.summary_info())  #assertion!
        assert "Total: $0.00" in overview.summary_info()
        self.reset_page()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("TearDown complete.")
