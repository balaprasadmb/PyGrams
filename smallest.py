'''
Created on 25-Oct-2023

@author: bborade
'''
s = None
print("B: ", s)
for i in [3, 41, 12, 9, 74, 15]:
    if s is None or i < s:
        s = i
        break
    print("L:", i, s)
print("S: ", s)