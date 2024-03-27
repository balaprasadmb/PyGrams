'''
Created on Nov 15, 2022

@author: bborade
'''
import math
inflation_rate = 0.08
pay_perios = 18.0
present_cash = 500000.0

print("Future Value(You'r Short Of): " + str(present_cash*(math.pow(1.0+inflation_rate,pay_perios))))
