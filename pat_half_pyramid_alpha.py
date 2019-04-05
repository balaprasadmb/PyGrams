def main():
  n = input()
  for l in range(n):
    for s in range(n-(l+1)):
      print ' ',
    for c in range(l+1):
      print chr(65+l),
    print
main()
