def get_jumps(jump, slide, wall_heights):
  jumps = []
  for index in range(len(wall_heights)):
    jumps.append(0)
    temp = 0
    if jump >= wall_heights[index]:
      jumps[index] +=1
    else:
      while temp < wall_heights[index]:
        if temp == 0:
          temp += jump
        else:
          temp = (temp-slide) + jump
        jumps[index] += 1
  return sum(jumps)


ip1 = int(raw_input('Enter activist jump: '))
ip2 = int(raw_input('Enter slide down by: '))
ip3_count = int(raw_input('How many walls: '))
ip3 = []
for wall in range(1, ip3_count + 1):
   ip3.append(int(raw_input('Enter height of wall %d: '%(wall))))
print 'Required jumps are: ' + str(get_jumps(ip1, ip2, ip3))
