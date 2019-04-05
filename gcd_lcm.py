def gcd(x, y):
    """This function implements the Euclidian algorithm
    to find G.C.D. of two numbers"""

    while(y):
        x, y = y, x % y

    return x

# define lcm function
def lcm(x, y):
    """This function takes two
    integers and returns the L.C.M."""

    lcm = (x*y)//gcd(x,y)
    return lcm

# change the values of num1 and num2 for a different result
num1 = 4
num2 = 16 

# uncomment the following lines to take input from the user
#num1 = int(input("Enter first number: "))
#num2 = int(input("Enter second number: "))

print "The G.C.D. of", num1,"and", num2,"is", gcd(num1, num2)
print "The L.C.M. of", num1,"and", num2,"is", lcm(num1, num2)