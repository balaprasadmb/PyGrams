'''
Created on Jan 7, 2021

@author: balaprsad
'''
import json
import os

f= open(os.path.abspath(os.path.dirname(__file__)) +"/data_files/session.json", 'r')
#data = json.loads(f.read())
data = json.load(f)
print(data)
