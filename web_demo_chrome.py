import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

browser = webdriver.Chrome(executable_path=os.path.abspath(os.path.dirname(__file__) + '\drivers\chromedriver'))
# browser = webdriver.Chrome(executable_path=os.path.abspath(os.path.dirname(__file__) + '/drivers/chromedriver'))
print(browser.capabilities)
browser.get('https://www.webroot.com/services/popuptester1.htm')
handles = browser.get_window_handles()
print(browser.title())
print(len(handles))
browser.close()