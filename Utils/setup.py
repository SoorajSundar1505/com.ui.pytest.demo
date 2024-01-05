from selenium import webdriver
import os


def setup_Browser(browser_name):
    if browser_name=='chrome':
            driver=webdriver.Chrome()
    elif browser_name=='firefox':
        driver=webdriver.Firefox()
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")
    driver.maximize_window()
    return driver

     
        
    