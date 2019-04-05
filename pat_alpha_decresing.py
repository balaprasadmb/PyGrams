def main():
  num = int(raw_input())
  for i in range(num, 0, -1):
    for j in range(num, num-i, -1):
      print chr(j+64),
    print

main()
