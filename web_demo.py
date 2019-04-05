'''
@author: bborade
'''
import os
import time
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


# os.environ["PATH"] += os.pathsep + os.path.abspath(os.path.dirname(__file__) +  '/data')
# os.environ["PATH"] += os.pathsep + os.path.abspath(os.path.dirname(__file__) +  '/geckodriver15')
# print os.getenv("PATH")

#binary = FirefoxBinary(r'/usr/bin/firefox')


# 
# print os.path.abspath(os.path.dirname(__file__) + "/geckodriver15/geckodriver")




# driver = webdriver.Firefox(capabilities=caps)
# driver = webdriver.Firefox()

def google():
#     sel = Selenium2Library.Selenium2Library()
    caps = DesiredCapabilities.FIREFOX.copy()
    caps["marionette"] = True
    driver = webdriver.Firefox(capabilities=caps, executable_path=os.path.abspath(os.path.dirname(__file__) + "/data/geckodriver"))
    driver.get("https://www.google.com")
    print driver.title
    try:
        assert 'Bala' in driver.page_source
    except Exception:
#         driver.save_screenshot(os.path.abspath(os.path.dirname(__file__) + '/screenshots/' + driver.title))
#         sel.capture_page_screenshot()
        raise Exception
    time.sleep(10)
    driver.quit()

# driver = webdriver.Chrome()
google()