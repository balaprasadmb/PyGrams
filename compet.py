import sys
import os

def uncommonBetweenCommon(input1,input2):
  set1 = set(input1)
  set2 = set(input2)
  diffs = set1 - set2
  print diffs
  final_string = ''
  for element in diffs:
    if final_string == '':
      final_string += str(element)
    else:
      final_string += '$' + str(element)
  return final_string

ip1_cnt = 0
ip1_cnt = int(raw_input())
ip1_i=0
ip1 = []
while ip1_i < ip1_cnt:
    ip1_item = int(raw_input());
    ip1.append(ip1_item)
    ip1_i+=1
ip2_cnt = 0
ip2_cnt = int(raw_input())
ip2_i=0
ip2 = []
while ip2_i < ip2_cnt:
    ip2_item = int(raw_input());
    ip2.append(ip2_item)
    ip2_i+=1
output = uncommonBetweenCommon(ip1,ip2)
print(str(output))

'''6: 
5
<br>
1
<br>
2
<br>
3
<br>
4
<br>
5
<br>
5
<br>
3
<br>
4
<br>
5
<br>
6
<br>
7
'''
