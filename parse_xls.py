import json
import csv
import collections

with open('file.txt') as f:
    st = f.read()

# print(st)

data = json.loads(st)
row = []
lis = ["4.40", "4.41", "4.42", "1.1", "1.2", "1.3", "2.1", "2.2", "2.3", "3.1", "3.2", "3.3", "3.4", "3.5", "3.6",
       "3.7", "3.8", "3.23", "4.1", "4.2", "4.3", "4.4", "4.5", "4.6", "4.7", "4.8", "4.9", "4.10", "4.11", "4.13",
       "4.15", "4.16", "4.17", "4.18", "4.19", "4.20", "4.21", "4.22", "4.23", "4.24", "4.25", "4.26", "4.27", "4.28",
       "4.29", "4.30", "4.31", "4.32", "4.34", "4.39", "4.43", "4.45", "4.69", "4.70", "4.75", "4.79", "5.1", "5.2",
       "5.3", "5.4", "5.5", "5.6", "5.7", "5.8", "5.9", "6.1", "6.2", "6.3", "6.4", "6.5", "6.6", "6.7", "6.8", "6.9",
       "6.10", "6.11", "6.17", "6.18", "6.19", "6.20", "6.21", "6.22", "6.23", "6.24", "6.25", "6.26", "6.27", "7.1",
       "7.2", "7.3", "7.4", "7.5", "7.8", "7.9", "3.19", "3.21", "4.36", "4.46", "4.47", "4.52", "5.13", "8.1"]

# with open('fields.txt', 'w') as f:
#     f.write(str(lis))

f = csv.writer(open('file1.csv', 'w'))
count = 0

print(data["4.15"])
if data['4.3'] == "6":
    row.append("EMV")
elif data['4.3'] == "3":
    row.append("Keyed")
elif data['4.3'] == "2" or data['4.3'] == "4":
    row.append("Swipe")
else:
    row.append("")

if data["4.15"] == "1":
    row.append("Credit")
elif data["4.15"] == "3":
    row.append("Debit")
elif data["4.15"] == "4":
    row.append("Gift")
else:
    row.append("")

data["3.23"] = "10.30.10.58:8000"

for l in lis:
    if l in data.keys():
        row.append(str(data[l]))
    else:
        row.append("")

lis1 = ["EntryType", "CardType"]
lis = lis1 + lis
f.writerow(lis)
f.writerow(row)
