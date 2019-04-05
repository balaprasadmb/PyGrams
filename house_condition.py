def house_condition(input1,input2):
    pass

ip1_cnt = 0
ip1_cnt = int(raw_input())
ip1_i=0
ip1 = []
while ip1_i < ip1_cnt:
    ip1_item = int(raw_input());
    ip1.append(ip1_item)
    ip1_i+=1
ip2 = int(raw_input());
output = house_condition(ip1,ip2)
print(str(output))