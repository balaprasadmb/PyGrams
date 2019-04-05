def main():
  n = input()
  for l in range(n):
    s = (n-l)-1
    for i in range(l+1):
      print s,
      s += 1
    print
  for l in range(n-1):
    s = l+1
    for i in range(n-(l+1)):
      print s,
      s += 1
    print

main()
