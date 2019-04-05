#0 1 2 3 4
#0 1 2 3 4
#0 1 2 3 4
#0 1 2 3 4
#0 1 2 3 4
#lower left
##40
##30 41
##20 31 42
def word_count(input1,input2):
  count = 0
  for item in input1:
    s = ''.join(item)
    if input2 in s:
      count += 1
  l1 = []
  for r in range(len(input1)):
    for c in range(len(input1)):
      if(c==0):
        l1.append(input1[c][r])
      else:
        l1[r] += input1[c][r]
  for item in l1:
    if input2 in item:
      count += 1

  return count

ip1_rows = 0
ip1_cols = 0
ip1_rows = int(raw_input())
ip1_cols = int(raw_input())
ip1 = []
for ip1_i in xrange(ip1_rows):
    ip1_temp = map(str,raw_input().strip().split(' '))
    ip1.append(ip1_temp)
try:
    ip2 = raw_input()
except:
    ip2 = None
output = word_count(ip1,ip2)
print(str(output))
