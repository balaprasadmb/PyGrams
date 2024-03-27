import json

data = {}

with open("request.json") as f:
	data = json.load(f)
	f.close()
print data

s='{'


for key in sorted(data):
    s+= '"' + str(key) + '"' + ':' + '"' + str(data[key]) + '",'

s= s.rstrip(',') + '}'

print '\n' + s
