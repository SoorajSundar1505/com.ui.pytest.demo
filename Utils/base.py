import os
import allure
from allure_commons.types import AttachmentType

class BasePage:
    def __init__(self,driver) :
        self.driver=driver
        

    def capture_screenshot(self,screenshotName):
        # screenshots_dir = os.path.join(os.getcwd(), 'screenshots')
        # if not os.path.exists(screenshots_dir):
        #     os.makedirs(screenshots_dir)

        # screenshot_path = os.path.join(screenshots_dir, f'{name}.png')
        # self.driver.save_screenshot(screenshot_path)

        # Attach the screenshot to the Allure report
        # allure.attach(self.driver.get_screenshot_as_png(), name=name, attachment_type=allure.attachment_type.PNG)
        allure.attach(self.driver.get_screenshot_as_png(),name=screenshotName,attachment_type=AttachmentType.PNG)

        # return screenshot_path