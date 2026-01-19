import pytest
from src.pages.login_page import LoginPage
from src.pages.products_page import ProductsPage

@pytest.mark.ui
def test_add_to_cart(driver):
    login_page = LoginPage(driver)
    login_page.navigate_to_login()
    login_page.enter_username()
    login_page.enter_password()
    login_page.click_login()
    products_page = ProductsPage(driver)
    products_page.click_add_to_cart_button("Sauce Labs Backpack")
    assert products_page.is_add_to_cart_button_clicked("Sauce Labs Backpack")