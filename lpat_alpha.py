def main():
  n = input()
  for l in range(n):
    for i,j in zip(range(l + 1), range(n-1, -1, -1)):
      print chr(65+j),
    print
  for l in range(n-1):
    for i,j in zip(range(l-1, -1,-1),range(n-1, -1, -1)):
      print chr(65+i),
    print
main()
