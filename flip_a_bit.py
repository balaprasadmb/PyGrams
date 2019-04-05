def nochange_bits(input1,input2,input3):
    pass
    
try:
    ip1 = raw_input()
except:
    ip1 = None
ip2 = int(raw_input());
ip3 = int(raw_input());
output = nochange_bits(ip1,ip2,ip3)
print(str(output))