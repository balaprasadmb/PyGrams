s = raw_input('Enter the String([Enter] to default): ')
if s == '':
  s = 'We are BMB Corp! Please mail us at info@bmbcorp.co.in'
print s
r = ''
l = []

for i in s:
  if not i.isalnum():
    print l[::-1]
    r += ''.join(l[::-1]) + i
    print r
    l = []
  else:
    l.append(i)
print r + ''.join(l[::-1])
  
    
