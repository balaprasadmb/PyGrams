'''
Created on Feb 28, 2022

@author: bborade
'''
import os
import xlrd

keys_template = []
raw_data = []
workbook = xlrd.open_workbook(os.path.dirname(__file__) + '/data_files/UAT_Test_Data.xlsx')
sheet = workbook.sheet_by_index(0)
for value in sheet.row_values(1):
    keys_template.append(str(value))
print(keys_template)
for row in range(2, sheet.nrows):
    if sheet.cell(row, 0).value == "Regis":
        raw_data.append({keys_template[column]: str(sheet.cell(row, column).value) 
                         for column in range(0, sheet.ncols) if keys_template[column] != ''})
print(raw_data)
