n = input('Enter Size: ')
c = raw_input('Enter Char or Word: ')
if n < 1 and len(c) < 1:
  print 'invalid'
elif n == 1:
  print c
else:
  for i in range(n):
    for j in range(i*2):
      print c,
    spaces=0
    if i != n/2:
      spaces = n//4
    for x in range(1, spaces):
      for y in range(x):
        print ' ',
    for k in range(i*2):
	  print c,
    print
