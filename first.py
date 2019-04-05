for i in range(10):
  row = ''
  for j in range(1,11):
    n = i * 10 + j
    t = str(n) + '\t'
    if n % 3 == 0 and n % 5 == 0:
      t = 'BalaPrasad\t'
    elif n % 3 == 0:
      t = 'Bala\t'
    elif n %5 ==0:
      t = 'Prasad\t'
    row += t
  print row

