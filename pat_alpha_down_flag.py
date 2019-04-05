def main():
  n = input()
  c = n + (n-2)
  for l in range(0, n):
    for i in range(0, l): 
      print ' ',
    for j in range(0, n-l):
      print chr(c + 65),
    for k in range(n-l, 1, -1):
      print chr(c + 65),
    c -= 2
    print

main()
