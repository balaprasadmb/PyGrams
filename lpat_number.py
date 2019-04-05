def main():
  n = input()
  for l in range(n):
    for i in range(n, (n-1)-l, -1):
      print i-1,
    print
  for l in range(n, 1, -1):
    for i in range(n, n-(l-1), -1):
      print i-1,
    print


main()
