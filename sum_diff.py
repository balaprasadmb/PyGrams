r = input("Enter Rows: ")
c = input("Enter Columns: ")
l=[]
for _ in range(r):
    t = []
    for _ in range(c):
        t.append(input("Enter Element: "))
    l.append(t)

d1 = 0
d2 = 0

l1 = []
l2 = []

for i in range(r):
    for j in range(c):
        if i == j:
            l1.append(l[i][j])
            d1 += l[i][j]
        if i == c-j-1:
            l2.append(l[i][j])
            d2 += l[i][j]
print l
print l1, "Sum of Major/Primary Diagonal: ", d1
print l2, "Sum Minor/secondary Diagonal: ", d2