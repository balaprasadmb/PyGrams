'''
Created on Apr 8, 2021

@author: bborade
'''
import uuid
import urllib
import urllib3
import requests

#url = "https://www.bing.com/th?id=OHR.AmboliFalls_EN-IN0634556638_1920x1200.jpg&rf=LaDigue_1920x1200.jpg"

#print(str(url).split("/")[-1])

#urllib.request.urlretrieve(url, str(url).split("/")[-1])

url = "https://www.instagram.com/p/CNZixK3B57b/?igshid=gdrlw12whbbs"

print(str(url).split("/")[-1])

res = urllib.request.urlopen(url, {"access_token":""})

pgs = res.loads()

urllib.request.urlretrieve(url, str(url).split("/")[-1])
