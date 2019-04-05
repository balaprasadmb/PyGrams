def main():
  num = int(raw_input())
  for i in range(num):
    s = ''
    for j in range(num-(i+1)):
      print ' ',
    for k in range((i*2)+1):
      s += ' ' + chr(65 + i)
    print s.strip()

main()
