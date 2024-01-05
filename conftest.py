from Utils.setup import setup_Browser
from selenium.webdriver.common.by import By
import pytest 

@pytest.fixture(scope="session")
def login():
    # initialise = initialize()
    browser = setup_Browser("chrome")
    browser.get("https://opensource-demo.orangehrmlive.com")
    browser.implicitly_wait(15)
    browser.find_element(By.XPATH, "//input[@name='username']").send_keys("Admin")
    browser.find_element(By.XPATH, "//input[@name='password']").send_keys("admin123")
    browser.find_element(By.XPATH,"//button[@type='submit']").click()
    browser.implicitly_wait(10)
    yield browser
    browser.quit()
