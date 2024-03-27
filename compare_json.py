import os
import json

print(os.path.dirname(__file__))

af = open(os.path.abspath(os.path.dirname(__file__)) +"/data_files/act.json", 'r')
ef = open(os.path.abspath(os.path.dirname(__file__)) + "/data_files/exp.json", 'r')

act = json.load(af)
exp = json.load(ef)

#a1 = list(act.keys())
#e1 = list(exp.keys())

#a1.sort()
#e1.sort()

ak = set(act.keys())
ek = set(exp.keys())

#print('Actual Keys: ',ak)
#print('Expected Keys: ',ek)


common_keys = ak.union(ek)

#print('Comman Keys: ', common_keys)

diff_keys = ak.intersection(ek)

print('Difference: ', diff_keys)

for k in sorted(diff_keys):
    print(k + '\t' + act[k] + '\t\t' + exp[k])

#print(ak.difference(ek))

#print(ek.difference(ak))

adds = []
print("Please Add Below Keys: ")
for k in ek.difference(ak):
    adds.append(k)
adds.sort()    
for k in adds:
    print(k + ':' + exp[k])
print(adds)

rems = []
print("Please Remove Below Keys: ")
for k in ak.difference(ek):
    rems.append(k)
#    print(k + ':' + act[k])
print(rems)
#['__and__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']
