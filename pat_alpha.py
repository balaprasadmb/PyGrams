def main():
  num = int(raw_input())
  for i in range(num,0,-1):
    c = 65
    s = chr(c)
    for j in range(1,i):
      s += ' ' + chr(c+j)
    print s

main()
