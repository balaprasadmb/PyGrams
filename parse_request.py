import json

data = {}

with open("request.json") as f:
	data = json.load(f)
	f.close()
d = {}
key = ''
if data.has_key('response'):
	key = 'response'
else:
	key = 'payload'
d = json.loads(data[key].strip('STX').strip('ETX').decode('hex'))

print d
s='{'

for key in sorted(d):
    s+= '"' + str(key) + '"' + ':' + '"' + str(d[key]) + '",'
s= s.rstrip(',') + '}'
print '\n' + s
