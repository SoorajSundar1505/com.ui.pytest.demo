from selenium.webdriver.common.by import By
from Utils.base import BasePage
class AdminPage:
    
    def __init__(self, driver):
        self.driver = driver
        self.base_page = BasePage(driver)
        
    def navigateToAdminPage(self):
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH,"//span[text()='Admin']").click()
        title = self.driver.find_element(By.XPATH, "//h6[text()='Admin']")
        assert title.is_displayed()
        self.base_page.capture_screenshot("verify_admin_page")

