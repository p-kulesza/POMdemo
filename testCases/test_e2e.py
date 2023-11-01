import unittest

from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium import webdriver

from Pages.checkoutPage import CheckoutPage
from Pages.completePage import CompletePage
from Pages.homePage import HomePage
from Pages.informationPage import InformationPage
from Pages.loginPage import LoginPage
from Pages.overviewPage import OverviewPage


class E2eTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        service_obj = Service("C:\\Users\\Admin\\Desktop\\geckodriver-v0.33.0-win64\\geckodriver.exe")
        options = webdriver.FirefoxOptions()
        options.add_argument("--headless")
        cls.driver = webdriver.Firefox(service=service_obj, options=options)
        cls.driver.implicitly_wait(5)
        print("SetUp complete.")

    def test_valid_e2e(self):
        driver = self.driver
        loginpage = LoginPage(driver)
        homepage = HomePage(driver)
        checkout = CheckoutPage(driver)
        information = InformationPage(driver)
        overview = OverviewPage(driver)
        complete = CompletePage(driver)
        driver.get("https://www.saucedemo.com/")
        assert "Swag Labs" in loginpage.logo_text()
        loginpage.enter_login("standard_user")
        loginpage.enter_password("secret_sauce")
        loginpage.click_login()
        items = driver.find_elements(By.XPATH, "//div[@class='inventory_item_description']")

        for item in items:
            if item.find_element(By.XPATH, "div/a/div").text == "Sauce Labs Onesie":
                item.find_element(By.XPATH, "div/button").click()
            if item.find_element(By.XPATH, "div/a/div").text == "Sauce Labs Fleece Jacket":
                item.find_element(By.XPATH, "div/button").click()

        homepage.click_checkout()
        assert "Sauce Labs Onesie", "Sauce Labs Fleece Jacket" in checkout.item_name_text()
        checkout.click_checkout()
        information.enter_firstname("AAA")
        information.enter_lastname("BBB")
        information.enter_zip("123")
        information.click_continue()
        assert "Total: $62.62" in overview.summary_info()
        assert "Sauce Labs Onesie", "Sauce Labs Fleece Jacket" in overview.get_item_name_text()
        overview.click_finish()
        assert "Thank you for your order!" in complete.complete_header_text()
        complete.click_back_home()
        assert "Swag Labs" in homepage.app_logo_presence()
        homepage.click_menu()
        homepage.menu_correctnes()
        homepage.click_checkout()
        self.assertEqual(checkout.list_number_of_items(), 0)
        checkout.click_continue_shopping()
        homepage.click_menu()
        homepage.click_logout()
        loginpage.click_login()
        assert "Epic sadface: Username is required" in loginpage.error_text()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("TearDown complete.")
