def main():
  n = input()
  for i in range(n):
    s = ''
    for j in range(n-(i+1)):
      print ' ',
    for k in range((i*2)+1):
      s += ' ' + str((i*2)+1)
    print s.strip()
main()
