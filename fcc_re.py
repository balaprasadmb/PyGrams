'''
Created on 25-Oct-2023

@author: bborade
'''
import re

s='A message from csev@umich.edu to cwen@iupui about meeting @2PM'

lst = re.findall("\\S+@\\S+", s)

print(lst)