import unittest

from selenium import webdriver
from selenium.webdriver.firefox.service import Service

from Pages.checkoutPage import CheckoutPage
from Pages.completePage import CompletePage
from Pages.homePage import HomePage
from Pages.informationPage import InformationPage
from Pages.loginPage import LoginPage
from Pages.overviewPage import OverviewPage


class CompletePageTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        service_obj = Service("C:\\Users\\Admin\\Desktop\\geckodriver-v0.33.0-win64\\geckodriver.exe")
        options = webdriver.FirefoxOptions()
        options.add_argument("--headless")
        cls.driver = webdriver.Firefox(service=service_obj, options=options)
        cls.driver.implicitly_wait(5)
        print("SetUp complete.")

    def allsteps(self):
        driver = self.driver
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
        homepage.click_checkout()
        checkout.click_checkout()
        information.enter_firstname("Piotr")
        information.enter_lastname("Kowalski")
        information.enter_zip("11-111")
        information.click_continue()
        overview.click_finish()



    def test_header_presence(self):
        driver = self.driver
        self.allsteps()
        completepage = CompletePage(driver)
        completepage.complete_header_presence()

    def test_back_home(self):
        driver = self.driver
        self.allsteps()
        completepage = CompletePage(driver)
        completepage.click_back_home()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("TearDown complete.")