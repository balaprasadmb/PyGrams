r = 3

c = 3

m = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print m

print '\nUpper Triangular Matrix'
for i in range(r):
    for j in range(c):
        if i <= j:
            print m[i][j],
        else:
            print ' ',
    print ''

print '\nLower Triangular Matrix'
for i in range(r):
    for j in range(c):
        if i >= j:
            print m[i][j],
        else:
            print ' ',
    print ''
print zip(*m)

print [[m[row][col] for row in range(c)] for col in range(r)]

for i in range(r):
    for j in range(c):
        if i < j:
            t = m[j][i]
            m[j][i] = m[i][j]
            m[i][j] = t
print m
