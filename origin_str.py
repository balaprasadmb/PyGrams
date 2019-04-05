def orignial(input1):
  length = len(input1)
  org_str = []
  org_str.append(input1[length])
  for i in range(length):
    temp = ''
    print org_str
    for i in range(length-1):
      if mid != i:
        temp += input1[i]
      print temp
    input1 = temp
  return org_str

try:
    ip1 = raw_input()
except:
    ip1 = None
output = orignial(ip1)
print(str(output))
'''
abcde
c
abde
cb
ade
cbd
ae
cbdae
-----
c
bdae
bc
dae
bcd
ae
abcde
-----

'''












