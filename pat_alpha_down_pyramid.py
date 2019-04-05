def main():
  n = input()
  for l in range(0, n):
    for i in range(0, l): 
      print ' ',
    for j in range(n-l,0,-1):
      print chr(65+(n-(l+1))),
    for k in range(n-l,1,-1):
      print chr(65+(n-(l+1))),
    print
main()
