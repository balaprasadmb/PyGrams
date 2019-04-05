def orignial(input1):
  l = []
  f = True
  l.append(input1[0])
  input1 = input1.lstrip(input1[0])
  op_str = ''
  for i in input1:
    if f:
      l.insert(0, i)
      f = False
    else:
      l.append(i)
      f = True
    input1.lstrip(i)
  return ''.join(l)
  
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
abcd
b
acd
bc
ad
bcad
-----
b
cad

'''
