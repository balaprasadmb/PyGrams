def main():
  num = int(raw_input())
  for i in range(num):
    s = ''
    for j in range(num-(i+1)):
      print ' ',
    cnt = 1
    for k in range((i*2)+1):
      s += ' ' + str(cnt)
      cnt += 1
    print s.strip()

main()
