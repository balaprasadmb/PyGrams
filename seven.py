def nochange_bits(input1,input2,input3):
  change=''
  input_len = len(input1)
  if input2 <= 0 and input3 <=0:
    return -1
  else:
    counter = 0
    for i in input1:
      if counter < input2:
        if i == '0':
          change+='1'
        else:
          change+='0'
      else:
        change += i
      counter += 1
    change = change.lstrip('0')
    op_len = len(change)
    change2 = ''
    counter = 0
    for i in change:
      if counter < input3:
        print '1'
        if i == '0':
          change2+='1'
        else:
          change2+='0'
      else:
        change2+= i
      counter += 1
    change2 = change2.lstrip('0').rjust(input_len, 'x')
    cnt = 0
    for i in range(input_len-1, 0, -1):
      if input1[i] == change2[i]:
        cnt += 1
      else:
        break
  return cnt

try:
    ip1 = raw_input()
except:
    ip1 = None
ip2 = int(raw_input());
ip3 = int(raw_input());
output = nochange_bits(ip1,ip2,ip3)
print(str(output))
      
#10110101101
#01010101101
#01010101101:3
#x0101101101:4
#3
#4
#6
