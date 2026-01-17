import pytest
from src.pages.login_page import LoginPage


@pytest.mark.ui
def test_login_page_displayed(driver):
    login_page = LoginPage(driver)
    login_page.navigate_to_login()
    
    assert login_page.is_username_field_displayed()
    assert login_page.is_password_field_displayed()
    assert login_page.is_login_button_displayed()

