from playwright.sync_api import Page, expect, Locator
from config.credentials import BASE_URL, USERNAME, PASSWORD


class LoginPage:
    """
    Playwright Page Object Model for Application Login Page
    """
    
    def __init__(self, page: Page):
        """
        Initialize the LoginPage with a Playwright Page object.
        Args:
            page: Playwright Page instance (from pytest-playwright fixture)
        """
        self.page = page
        self.timeout = 10000  # 10 seconds timeout for assertions
        self.username_input = self.page.locator("#user-name")
        self.password_input = self.page.locator("#password")
        self.login_button = self.page.locator("#login-button")
    
    def navigate_to_login(self):
        """
        Navigate to the Application login page.
        
        Why: Uses Playwright's goto() method which automatically waits for page load and network idle.
        """
        self.page.goto(BASE_URL)
    
    def is_username_field_displayed(self):
        try:
            expect(self.username_input).to_be_visible(timeout=self.timeout)
            return True
        except:
            return False
    
    def is_password_field_displayed(self):
        try:
            expect(self.password_input).to_be_visible(timeout=self.timeout)
            return True
        except:
            return False
    
    def is_login_button_displayed(self):
        try:
            expect(self.login_button).to_be_visible(timeout=self.timeout)
            return True
        except:
            return False
    
    def enter_username(self, username: str = None):
        username_value = username or USERNAME
        self.username_input.fill(username_value)
    
    def enter_password(self, password: str = None):
        password_value = password or PASSWORD
        self.password_input.fill(password_value)
    
    def click_login(self):
        self.login_button.click()
