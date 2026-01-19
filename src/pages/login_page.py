from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.credentials import SAUCEDEMO_URL, USERNAME, PASSWORD


class LoginPage:
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def navigate_to_login(self):
        self.driver.get(SAUCEDEMO_URL)
    
    def is_username_field_displayed(self):
        try:
            self.wait.until(EC.visibility_of_element_located(self.USERNAME_INPUT))
            return True
        except:
            return False
    
    def is_password_field_displayed(self):
        try:
            self.wait.until(EC.visibility_of_element_located(self.PASSWORD_INPUT))
            return True
        except:
            return False
    
    def is_login_button_displayed(self):
        try:
            self.wait.until(EC.visibility_of_element_located(self.LOGIN_BUTTON))
            return True
        except:
            return False

    def enter_username(self):
        self.wait.until(EC.visibility_of_element_located(self.USERNAME_INPUT)).send_keys(USERNAME)
    
    def enter_password(self):
        self.wait.until(EC.visibility_of_element_located(self.PASSWORD_INPUT)).send_keys(PASSWORD)
    
    def click_login(self):
        self.wait.until(EC.element_to_be_clickable(self.LOGIN_BUTTON)).click()

