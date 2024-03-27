import json

s = raw_input("Enter the Json String: ")

print s

spilts = s.split(',')

print spilts

d = {}

for element in spilts:
	t=[]
	t= element.split(':')
	d[t[0].strip('"')] = t[1].strip('"')

print sorted(d)

