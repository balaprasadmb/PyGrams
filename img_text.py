'''
Created on Aug 19, 2022

@author: bborade
'''
import os

from PIL import Image

from pytesseract import pytesseract

path=input("Enter path to image: ")

img = Image.open(path)

text = pytesseract.image_to_string(img)

print(text)
