def main():
  num = input()
  for l in range(0, num):
    for i in range(0,l): 
      print ' ',
    for j in range(0,num-l):
      print '*',
    for k in range(num-l,1,-1):
      print '*',
    print
      
main()
