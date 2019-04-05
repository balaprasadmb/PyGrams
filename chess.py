def getStepCount(input1,input2,input3,input4):
  xdiff = input3 - input1
  ydiff = input4 - input2
  if xdiff == ydiff:
    if xdiff > 0 and ydiff > 0:
      return xdiff
    else:
      return abs(xdiff + ydiff)
  else:
      return abs(xdiff - ydiff)

ip1 = int(raw_input('Enter x1: '))
ip2 = int(raw_input('Enter y1: '))
ip3 = int(raw_input('Enter x2: '))
ip4 = int(raw_input('Enter y2: '))
output = getStepCount(ip1,ip2,ip3,ip4)
print(str(output))

#3 1 5 2
# 2 1
#5 1 #
