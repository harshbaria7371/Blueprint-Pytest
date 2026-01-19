from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.credentials import SAUCEDEMO_URL

class ProductsPage:
    PRODUCTS_TITLE = (By.XPATH, "//span[@data-test='title']")
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def is_products_title_displayed(self):
        try:
            self.wait.until(EC.visibility_of_element_located(self.PRODUCTS_TITLE))
            return True
        except:
            return False
    
    def get_add_to_cart_button_locator(self, product_name):
        """
        Returns a dynamic locator for the 'Add to cart' button of a specific product.
        
        Args:
            product_name (str): The name of the product
            
        Returns:
            tuple: A locator tuple (By, locator_string) for the Add to cart button
        """
        # XPath: Find the product by name, then locate the Add to cart button in the same container
        # This works by finding the product name text, going up to the inventory item container,
        # and then finding the button with 'add-to-cart' in its id, name, data-test attribute, or text
        xpath = (f"//div[contains(@class, 'inventory_item_name') and normalize-space(text())='{product_name}']"
                 f"/ancestor::div[contains(@class, 'inventory_item')]"
                 f"//button[contains(@id, 'add-to-cart') or contains(@name, 'add-to-cart') "
                 f"or contains(@data-test, 'add-to-cart') or contains(text(), 'Add to cart')]")
        return (By.XPATH, xpath)
    
    def click_add_to_cart_button(self, product_name):
        """
        Clicks the 'Add to cart' button for a specific product.
        
        Args:
            product_name (str): The name of the product whose 'Add to cart' button should be clicked
        """
        locator = self.get_add_to_cart_button_locator(product_name)
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def get_remove_button_locator(self, product_name):
        """
        Returns a dynamic locator for the 'Remove' button of a specific product.
        This button appears after the item has been added to cart.
        
        Args:
            product_name (str): The name of the product
            
        Returns:
            tuple: A locator tuple (By, locator_string) for the Remove button
        """
        # XPath: Find the product by name, then locate the Remove button in the same container
        xpath = (f"//div[contains(@class, 'inventory_item_name') and normalize-space(text())='{product_name}']"
                 f"/ancestor::div[contains(@class, 'inventory_item')]"
                 f"//button[contains(@id, 'remove') or contains(@name, 'remove') "
                 f"or contains(@data-test, 'remove') or contains(text(), 'Remove')]")
        return (By.XPATH, xpath)
    
    def is_add_to_cart_button_clicked(self, product_name):
        """
        Checks if the 'Add to cart' button for a specific product was clicked successfully.
        This is verified by checking if the 'Remove' button is now visible (which appears after adding to cart).
        
        Args:
            product_name (str): The name of the product whose 'Add to cart' button should be checked
            
        Returns:
            bool: True if the Remove button is visible (item was added), False otherwise
        """
        try:
            locator = self.get_remove_button_locator(product_name)
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except:
            return False