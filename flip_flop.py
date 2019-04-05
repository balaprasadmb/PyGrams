def replace_bits(input1, length):
  counter = 0
  change = ''
  for i in input1:
    if counter<length:
      print 'counter: '+str(counter)
      if i == '0':
        change+='1'
      else:
        change+='0'
    else:
      change += i
    counter += 1
  print 'change: ' + change
  return change.lstrip('0')

def nochange_bits(input1,input2,input3):
  change=''
  input_len = len(input1)
  if input2 <= 0 and input3 <=0:
    return -1
  else:
    change = replace_bits(input1, input2)
    op_len = len(change)
    change2 = replace_bits(change, input3).rjust(input_len, 'x')
    cnt = 0
    for i in range(input_len-1, 0, -1):
      print 'i: ' + str(i)
      print input1[i]
      print change2[i]
      if input1[i] == change2[i]:
        cnt += 1
      else:
        break
  print 'count: ' + str(cnt)
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
#01001010010
#01010101101
#x0101101101
#3
#4
#6
