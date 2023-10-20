from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.select import Select

from Pages.homePage import HomePage
from Pages.loginPage import LoginPage

service_obj = Service("C:\\Users\\user\\Desktop\\geckodriver\\geckodriver.exe")
driver = webdriver.Firefox(service=service_obj)
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://www.saucedemo.com/")
loginpage = LoginPage(driver)
homepage = HomePage(driver)
loginpage.enter_login("standard_user")
loginpage.enter_password("secret_sauce")
loginpage.click_login()
homepage.click_addtocart()
sel = Select(homepage.select_product_sort())
sel.select_by_visible_text()
