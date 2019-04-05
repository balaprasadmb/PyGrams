def main():
  num = int(raw_input())
  for i in range(num):
    s = ''
    for j in range(num-(i+1)):
      print ' ',
    for k in range(65+i, 64, -1):
      s += ' ' + chr(k)
    for x in range(66, 66+i):
      s += ' ' + chr(x)
    print s.lstrip()

main()
