def main():
  num = int(raw_input())
  count = 1
  for i in range(num,0,-1):
    s = str(count)
    for j in range(1, i):
      s += ' ' + str(count)
    print s
    count += 1
main()
