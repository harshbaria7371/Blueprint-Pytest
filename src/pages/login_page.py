from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.credentials import SAUCEDEMO_URL


class LoginPage:
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-butto")
    
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

