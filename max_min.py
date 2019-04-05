def alternateSorting(input1):
	input1 = sorted(input1)
	cnt = len(input1) 
	half_cnt = cnt//2
	l=[]
	for i in range(0, half_cnt):
		if i==0:
			l.append(input1[-1])
		else:
			l.append(input1[(0-i)-1])
		l.append(input1[i])
	if cnt%2!=0:
		l.append(input1[half_cnt])
	return l

#[1,2,3,4,5,6,7]
#0
#[7,1]

ip1_cnt = 0
ip1_cnt = int(raw_input())
ip1_i=0
ip1 = []
while ip1_i < ip1_cnt:
    ip1_item = int(raw_input());
    ip1.append(ip1_item)
    ip1_i+=1
output = alternateSorting(ip1)
print '\n'
for output_cur in output:
    print( str(output_cur))
