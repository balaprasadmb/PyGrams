def main():
  n = input()
  t = n + (n-1)
  for l in range(0, n):
    for i in range(0, l): 
      print ' ',
    for j in range(0, n-l):
      print t,
    for k in range(n-l,1,-1):
      print t,
    t -= 2
    print

main()
