a = [1, 2, 5, 9, 99, 100]
# a = [5, 19, 11, 2]
print a
b = [3, 7 , 19, 93]
# b = [39, 17, 2, 5, 7]
print b
c = []
c = sorted(a + b)
print c
d = []
ca = 0
cb = 0
for _ in range(len(a) + len(b)):
    if a[ca] < b[cb]:
        d.append(a[ca])
        ca += 1
        print 'a', ca
    else:
        d.append(b[cb])
        cb += 1
        print 'b', cb
    if ca >= len(a):
        for i in b[cb:]:
            d.append(i)
        break
    elif cb >= len(b):
        for j in a[ca:]:
            d.append(j)
        break
print d