def getTolls(input1,input2):
    

ip1 = int(raw_input());
ip2_cnt = 0
ip2_cnt = int(raw_input())
ip2_i=0
ip2 = []
while ip2_i < ip2_cnt:
    try:
        ip2_item = raw_input()
    except:
        ip2_item = None
    ip2.append(ip2_item)
    ip2_i+=1
output = getTolls(ip1,ip2)
for output_cur in output:
    print(str(output_cur))

