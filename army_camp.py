def validateRow(input1,input2):
    pass

try:
    ip1 = raw_input()
except:
    ip1 = None
try:
    ip2 = raw_input()
except:
    ip2 = None
output = validateRow(ip1,ip2)
print(str(output))