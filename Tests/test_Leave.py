from Pages.leavePage import LeavePage
from selenium.webdriver.common.by import By

class TestLeavePage:
    def test_leave_dashboard(self,login):
        leave_page = LeavePage(login)
        leave_page.navigateToLeavePage()
        title = login.find_element(By.XPATH,"//h6[text()='Leave']")
        assert title.is_displayed()
