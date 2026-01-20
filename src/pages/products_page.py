from playwright.sync_api import Page, expect, Locator
from config.credentials import BASE_URL


class ProductsPage:
    """
    Playwright Page Object Model for Application Products Page
    """
    
    def __init__(self, page: Page):
        """
        Initialize the ProductsPage with a Playwright Page object.
        Args:
            page: Playwright Page instance (from pytest-playwright fixture)
        """
        self.page = page        
        self.timeout = 10000  # 10 seconds timeout for assertions
        self.products_title = self.page.locator("span[data-test='title']")
    
    def is_products_title_displayed(self):
        try:
            expect(self.products_title).to_be_visible(timeout=self.timeout)
            return True
        except:
            return False
    
    def get_add_to_cart_button_locator(self, product_name: str) -> Locator:
        # XPath: Find the product by name, then locate the Add to cart button in the same container
        # This works by finding the product name text, going up to the inventory item container,
        # and then finding the button with 'add-to-cart' in its id, name, data-test attribute, or text
        xpath = (f"//div[contains(@class, 'inventory_item_name') and normalize-space(text())='{product_name}']"
                 f"/ancestor::div[contains(@class, 'inventory_item')]"
                 f"//button[contains(@id, 'add-to-cart') or contains(@name, 'add-to-cart') "
                 f"or contains(@data-test, 'add-to-cart') or contains(text(), 'Add to cart')]")
        return self.page.locator(xpath)
    
    def click_add_to_cart_button(self, product_name: str):
        locator = self.get_add_to_cart_button_locator(product_name)
        locator.click()
    
    def get_remove_button_locator(self, product_name: str) -> Locator:
        # XPath: Find the product by name, then locate the Remove button in the same container
        xpath = (f"//div[contains(@class, 'inventory_item_name') and normalize-space(text())='{product_name}']"
                 f"/ancestor::div[contains(@class, 'inventory_item')]"
                 f"//button[contains(@id, 'remove') or contains(@name, 'remove') "
                 f"or contains(@data-test, 'remove') or contains(text(), 'Remove')]")
        return self.page.locator(xpath)
    
    def is_add_to_cart_button_clicked(self, product_name: str):
        try:
            locator = self.get_remove_button_locator(product_name)
            expect(locator).to_be_visible(timeout=self.timeout)
            return True
        except:
            return False
