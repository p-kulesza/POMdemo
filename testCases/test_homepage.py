import unittest

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from Pages.homePage import HomePage
from Pages.loginPage import LoginPage


class HomePageTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        service_obj = Service("C:\\Users\\Admin\\Desktop\\geckodriver-v0.33.0-win64\\geckodriver.exe")
        cls.driver = webdriver.Firefox(service=service_obj)
        cls.driver.maximize_window()
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

    def test_reset(self):
        driver = self.driver
        homepage = HomePage(driver)
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
        homepage.list_number_of_items()

    def test_sort_a_to_z(self):
        driver = self.driver
        homepage = HomePage(driver)
        self.login_step()
        homepage.select_product_sort_visible_text("Name (A to Z)")
        #assertion here

    def test_sort_z_to_a(self):
        driver = self.driver
        homepage = HomePage(driver)
        self.login_step()
        homepage.select_product_sort_visible_text("Name (Z to A)")
        # assertion here

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