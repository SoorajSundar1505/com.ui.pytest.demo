from Pages.adminPage import AdminPage
from selenium.webdriver.common.by import By
from Tests.test_Leave import TestLeavePage
import pytest


class TestAdmin:

    @pytest.mark.order1
    @pytest.mark.sanity
    def test_admin_dashboard(self, login):
        admin_page = AdminPage(login)
        admin_page.navigateToAdminPage()
        
        

    # @pytest.mark.order1
    # @pytest.mark.others
    # def test_admin_dashboard_others(self, login):
    #     admin_page = AdminPage(login)
    #     admin_page.navigateToAdminPage()
    #     title = login.find_element(By.XPATH, "//h6[text()='Admin']")
    #     assert title.is_displayed()


    @pytest.mark.order2
    @pytest.mark.sanity
    def test_leave(self, login):
        test_leave_instance = TestLeavePage()
        test_leave_instance.test_leave_dashboard(login)