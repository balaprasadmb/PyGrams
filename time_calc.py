'''
Created on Oct 21, 2022

@author: bborade
'''
import os

import datetime
from datetime import timedelta

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options

driver_path = os.path.abspath(os.path.dirname(__file__) + '/drivers/chromedriver76_lin64')

chrome_options = Options()
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(executable_path = driver_path, options = chrome_options)

driver.get("https://10.200.10.50/")

WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'username')),
                                     'Login Page is not visible')

driver.find_element_by_css_selector('input#username').send_keys("emp1501")

driver.find_element_by_css_selector('input#password').send_keys("Leaves#1903")

driver.find_element_by_css_selector('button.button').click()

#driver.find_element_by_css_selector('#accordionmenu>ul.menu>li.item-610').click()

t_date = datetime.datetime.today().strftime('%Y-%m-%d')

wtime_popup_loc = 'https://10.200.10.50/index.php?com_hrm=&cmd=attendance.details&tmpl=component&userid={0}&date={1}&option=com_hrm'.format('2414', t_date)


#driver.find_element_by_css_selector('div[style="background-color:#00B3FB;border-color:#666666;color:#FFFFFF"]').click()

driver.get(wtime_popup_loc)

WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div#main')),
                                     'Attendence Details Popup Not Visible')

#driver.switch_to.frame(driver.find_element_by_css_selector('div#sbox-content'))

wtime = driver.find_element_by_css_selector('td.total-time:nth-child(2)').get_attribute('innerHTML').split('-')[1]

print(wtime)

# wtime_num = wtime[1] + '.'
# 
# for i in wtime[8:]:
#     if i.isdigit():
#         wtime_num += i
# 
# print(wtime_num)
# 
# wtime_num = float(wtime_num)
# 
# 
# 
# print("Your Remaning time is: " + str(8.00 - wtime_num))

driver.close()