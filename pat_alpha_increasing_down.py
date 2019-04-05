def main():
  n = input()
  c = n + (n-1)
  for l in range(0, n):
    for i in range(0, l): 
      print ' ',
    for j in range(0, c):
      print chr(j + 65),
    c -= 2
    print

main()
