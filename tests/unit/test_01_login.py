import pytest
from src.pages.login_page import LoginPage
from src.pages.products_page import ProductsPage


@pytest.mark.playwright
@pytest.mark.ui
def test_login_page_displayed(page_with_screenshot):
    login_page = LoginPage(page_with_screenshot)
    login_page.navigate_to_login()
    
    assert login_page.is_username_field_displayed()
    assert login_page.is_password_field_displayed()
    assert login_page.is_login_button_displayed()


@pytest.mark.playwright
@pytest.mark.ui
def test_login_page_login(page_with_screenshot):
    login_page = LoginPage(page_with_screenshot)
    login_page.navigate_to_login()

    login_page.enter_username()
    login_page.enter_password()
    login_page.click_login()

    products_page = ProductsPage(page_with_screenshot)
    assert products_page.is_products_title_displayed()
