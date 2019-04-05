def farms_division(input1):
  max1 = max(input1)
  max2 = -1
  mylist = []
  for i in input1:
    if i < 0:
      return 'invalid'
    mylist.append(i)
  mylist.remove(max1)
  sum1=0
  for i in range(0, len(mylist)):
    print 'max: ' + str(max1)
    print 'sum: ' + str(sum(mylist))
    if sum(mylist) == max1:
      return 'yes'
    else:
      max2 = max(mylist)
      mylist.remove(max2)
      max1 += max2
  return 'no'
	

ip1_cnt = 0
ip1_cnt = int(raw_input())
ip1_i=0
ip1 = []
while ip1_i < ip1_cnt:
    ip1_item = int(raw_input());
    ip1.append(ip1_item)
    ip1_i+=1
output = farms_division(ip1)
print(str(output))
