import pytest
import os
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


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


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Hook to capture test outcome for screenshot on failure"""
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
