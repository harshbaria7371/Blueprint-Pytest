import pytest
import os
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from playwright.sync_api import Page


@pytest.fixture(scope='function')
def driver(request):
    """Simple Selenium WebDriver fixture with screenshot on failure"""
    chrome_options = Options()
    # Add any Chrome options you need here
    # chrome_options.add_argument('--headless')  # Uncomment for headless mode
    
    driver = webdriver.Chrome(options=chrome_options)
    
    yield driver
    
    # Take screenshot on test failure
    if request.node.rep_call.failed:
        screenshot_dir = "screenshots"
        if not os.path.exists(screenshot_dir):
            os.makedirs(screenshot_dir)
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        test_name = request.node.name
        screenshot_path = os.path.join(screenshot_dir, f"{test_name}_{timestamp}.png")
        driver.save_screenshot(screenshot_path)
        print(f"\nScreenshot saved: {screenshot_path}")
    
    driver.quit()

@pytest.fixture(scope='function')
def page_with_screenshot(page: Page, request):
    """
    Extended Playwright page fixture with automatic screenshot on test failure. This fixture wraps pytest-playwright's built-in 'page' fixture and adds screenshot functionality similar to our Selenium driver fixture.
    """
    yield page
    
    if hasattr(request.node, 'rep_call') and request.node.rep_call.failed:
        screenshot_dir = "screenshots"
        if not os.path.exists(screenshot_dir):
            os.makedirs(screenshot_dir)
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        test_name = request.node.name
        screenshot_path = os.path.join(screenshot_dir, f"playwright_{test_name}_{timestamp}.png")
        
        try:
            page.screenshot(path=screenshot_path, full_page=True)
            print(f"\nPlaywright screenshot saved: {screenshot_path}")
        except Exception as e:
            print(f"\nFailed to save Playwright screenshot: {e}")


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Hook to capture test outcome for screenshot on failure"""
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
