from selenium.webdriver.common.by import By


class LoginPage():
    def __init__(self,driver):
        self.driver = driver
        self.textbox_login_id = "user-name"
        self.textbox_password_id = "password"
        self.button_login_id = "login-button"
        self.alert_error_xpath = "//h3[@data-test='error']"
        self.logo_css = ".login_logo"

    def enter_login(self, login):
        self.driver.find_element(By.ID, self.textbox_login_id).clear()
        self.driver.find_element(By.ID, self.textbox_login_id).send_keys(login)

    def enter_password(self, password):
        self.driver.find_element(By.ID, self.textbox_password_id).clear()
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.ID, self.button_login_id).click()

    def error_text_presence(self):
        assert self.driver.find_element(By.XPATH, self.alert_error_xpath)

    def logo_presence(self):
        assert self.driver.find_element(By.CSS_SELECTOR, self.logo_css)
