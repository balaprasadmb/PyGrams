def divideAndRule(input1):
  n = len(input1)
  for i in range(n):
    sum1 = 0
    sum2 = 0
    for j in range(i):
      sum1+=input1[j]
    for k in range(i+1, n):
      sum2+=input1[k]
    if sum1 == sum2:
      return 1
  return -1

ip1_cnt = 0
ip1_cnt = int(raw_input())
ip1_i=0
ip1 = []
while ip1_i < ip1_cnt:
    ip1_item = int(raw_input());
    ip1.append(ip1_item)
    ip1_i+=1
output = divideAndRule(ip1)
print(str(output))
