n = input("Enter the Number: ")
sum1 = 0
while n > 0:
    sum1 += n%10
    n /= 10

print sum1
