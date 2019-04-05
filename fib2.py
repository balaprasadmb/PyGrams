#!usr/bin/python
def fib(n):
    a, b = 0, 1
    while b < n:
        print b
        a, b = b, a + b

def fib2(n):
    l = []
    a, b = 0, 1
    while b < n:
        l.append(b)
        a, b = b, a + b
    return l

fib(1000)
print fib2(1000)