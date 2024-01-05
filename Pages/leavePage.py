from selenium.webdriver.common.by import By

class LeavePage:
    def __init__(self,driver):
        self.driver=driver
    
    def navigateToLeavePage(self):
        self.driver.find_element(By.XPATH,"//span[text()='Leave']").click()
        self.driver.implicitly_wait(10)
        