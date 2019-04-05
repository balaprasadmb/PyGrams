def main():
  num = int(raw_input())
  for i in range(1,num+1):
    for j in range(num-i):
      print ' ',
    for k in range(1, i+1):
      print k,
    print

main()
