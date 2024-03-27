'''
Created on Dec 10, 2021

@author: bborade
'''
import xlrd

xls1_path = "/home/bprasad/Workspace23/AuruspayRobot/auruspay/data/UAT_Test_Data.xlsx"
xls2_path = "/home/bprasad/Workspace23/AuruspayRobot/auruspay/data/UAT_Test_Data1.xlsx"

wb1 = xlrd.open_workbook(xls1_path)
wb2 = xlrd.open_workbook(xls2_path)

sheet1 = wb1.sheet_by_index(0)
sheet2 = wb2.sheet_by_index(0)

print("Sheet1:-\nRows: {}\nColumns: {}".format(sheet1.nrows, sheet1.ncols))
print("\nSheet2:-\nRows: {}\nColumns: {}".format(sheet2.nrows, sheet2.ncols))

# for r1,r2 in range(0, sheet1.nrows),range(0, sheet2.nrows):
#     for c1,c2 in range(0, sheet1.ncols),range(0, sheet2.ncols):
#         if sheet1.cell(r1, c1).value != sheet1.cell(r2, c2).value:
#             print("Data From Row1 {}, Column1 {}, Row2 {}, Column2 {} Doesn't Matches {}-{}".format(
#                 r1,c1,r2,c2,sheet1.cell(r1, c1).value, sheet1.cell(r2, c2).value))

for r in range(0, sheet1.nrows):
    for c in range(0, sheet2.ncols):
        if sheet1.cell(r, c).value != sheet2.cell(r, c).value:
            print("Data From Row {}, Column {} Doesn't Matches {}-{}".format(
                r,sheet2.cell(r, c),sheet1.cell(r, c).value, sheet2.cell(r, c).value))


