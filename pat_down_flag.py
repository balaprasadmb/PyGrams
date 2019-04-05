def main():
  num = int(raw_input())
  for i in range(0, num):
    for j in range(0,i): 
      print ' ',
    for k in range(0,num-i):
      print '*',
    print

main()
