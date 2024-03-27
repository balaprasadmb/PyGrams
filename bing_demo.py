import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait




caps = DesiredCapabilities.FIREFOX.copy()
caps["marionette"] = True
opts = Options()
# opts.headless = True
browser = webdriver.Firefox(capabilities=caps, options = opts,
                            executable_path = os.path.abspath(os.path.dirname(__file__) + '/drivers/geckodriver'))
print(browser.capabilities)

browser.get('http://www.bing.com')

assert 'Bing' in browser.page_source

WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'a#id_l')),
                                     'IFrame Element Not Visible')

browser.find_element_by_css_selector('a#id_l').click()

print(browser.title)

# browser.close()
