'''
Created on May 16, 2022

@author: bborade
'''
principal = 2300000

no_of_year = 12

rate = 9.20

print(float(principal * rate * float(1 + rate)) * no_of_year/(float(1 + rate) * no_of_year -1 ))

r = float(rate/12)/100

print((principal * r * (1 + r)) * no_of_year/((1 + r) * no_of_year -1 ))
'''20528677.474402733
18492.238016864318'''