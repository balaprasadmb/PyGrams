class Exp():

    def __init__(self, val):
        self.value = val


obj1 = Exp(1)
print obj1.value

obj2 = Exp(2)
print obj2.value

obj3 = Exp(3)
print obj3.value

obj4 = Exp(4)
print obj4.value

obj5 = Exp(5)
print obj5.value

l = [obj5, obj3, obj1, obj2, obj4]

print ""

for i in l:
    print i.value,

print ""
l.sort(key=lambda x:x.value)

# sort1 = lambda x:

# sort1(l)

for i in l:
    print i.value,