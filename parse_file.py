import json
d = {}

with open("bala.json") as f:
	d = json.load(f)
print '{'
for key in sorted(d):
	print '"' + str(key) + '"' + ':',
	if key!="8.1":
		print '"' + str(d[key]) + '",'
	else:
		print '"' + str(d[key]) + '"'
print '}'


