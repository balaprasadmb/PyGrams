def main():
  n = input()
  for l in range(1, n + 1):
    for i in range(l):
      print '*',
    print
  for l in range(n-1,0,-1):
    for i in range(l):
      print '*',
    print

main()
