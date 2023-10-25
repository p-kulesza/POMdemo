import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Pages.checkoutPage import CheckoutPage
from Pages.homePage import HomePage
from Pages.loginPage import LoginPage

class HomePageTest(unittest.TestCase):
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
        loginpage = LoginPage (driver)
        loginpage.enter_login("standard_user")
        loginpage.enter_password("secret_sauce")
        loginpage.click_login()
        print("Successfully logged in")

    def test_menu(self):
        driver = self.driver
        homepage = HomePage(driver)
        self.login_step()
        homepage.click_menu()
        #menu presence/menu correctness assertion
        homepage.menu_correctnes()

    def test_reset(self):
        driver = self.driver
        homepage = HomePage(driver)
        checkout = CheckoutPage(driver)
        self.login_step()
        homepage.click_addtocart()
        homepage.click_menu()
        homepage.click_reset()
        homepage.click_checkout()

        # add checkout assertion - lack of .cart_quantity?

    def test_allitems(self):
        driver = self.driver
        homepage = HomePage(driver)
        self.login_step()
        homepage.click_menu()
        homepage.click_allitems()  # This does nothing on page :(, no assertion
        homepage.app_logo_presence()

    def test_about(self):
        driver = self.driver
        homepage = HomePage(driver)
        self.login_step()
        homepage.click_menu()
        homepage.click_about()
        actualtitle = self.driver.title #about page name assertion
        expectedtitle = "Sauce Labs: Cross Browser Testing, Selenium Testing & Mobile Testing"
        self.assertEqual(actualtitle, expectedtitle)

    def test_logout(self):
        driver = self.driver
        homepage = HomePage(driver)
        loginpage = LoginPage(driver)
        self.login_step()
        homepage.click_menu()
        homepage.click_logout()
        loginpage.logo_presence()

    def test_number_of_items(self):
        driver = self.driver
        homepage = HomePage(driver)
        self.login_step()
        print("number of items on the page:")
        homepage.number_of_items()


    def test_sort_a_to_z(self):
        driver = self.driver
        homepage = HomePage(driver)
        homepage.select_product_sort_visible_text("Name (A to Z)")
        actualList = homepage.list_products()
        expectedList = sorted(homepage.list_products())
        self.assertEqual(actualList, expectedList) #no hardcode!!!!

    def test_sort_z_to_a(self):
        driver = self.driver
        homepage = HomePage(driver)
        homepage.select_product_sort_visible_text("Name (Z to A)")
        actualList = homepage.list_products()
        expectedList  = sorted(homepage.list_products(), reverse = True)
        self.assertEqual(actualList, expectedList)

    def test_sort_low_to_high(self):
        driver = self.driver
        homepage = HomePage(driver)
        self.login_step()
        homepage.select_product_sort_visible_text("Price (low to high)")
        # assertion here

    def test_sort_high_to_low(self):
        driver = self.driver
        homepage = HomePage(driver)
        self.login_step()
        homepage.select_product_sort_visible_text("Price (high to low)")
        # assertion here

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("TearDown complete.")
