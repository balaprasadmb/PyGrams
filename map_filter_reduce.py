def even(n):
    if n % 2 == 0:
        return True
    else:
        False

print map(even, range(1,10))
print filter(even, range(1,10))
print reduce(even, range(1,10))

'''map'''
items = [1, 2, 3, 4, 5]
squared = []
for i in items:
    squared.append(i**2)

print "Before:", squared

'''with map()'''
items = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, items))

print "After:", squared
    
'''filter'''
'''with filter()'''
number_list = range(-5, 5)

print "Before:", number_list

less_than_zero = list(filter(lambda x: x < 0, number_list))
print "After:", less_than_zero

'''filter'''
product = 1
for num in [1, 2, 3, 4]:
    product = product * num
print "Before:", product

'''with filter()'''
product = reduce((lambda x, y: x * y), [1, 2, 3, 4])

print "After:", product
