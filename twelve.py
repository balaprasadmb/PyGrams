def main():
  s = input()
  if type(s) is str:
    print 'This input is of type string.'
  elif type(s) is float:
    print 'This input is of type Float.'
  elif type(s) is int:
    print 'This input is of type Integer.'
  else:
    print 'This is something else.'
main()
