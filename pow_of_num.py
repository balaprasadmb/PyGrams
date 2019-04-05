''' Power of a Number (100 Marks)
Python.math module provides access to the mathematical functions defined by the C standard.
One of the widely used function is math.pow(x, y) which Returns x raised to the power y.
Now, you are given three integers x, y and M. You have to print ( x ^ y ) Mod M.

Input Format
First line will contain three integers x, y, and M.

Constraints
1 <= X <= 20
1 <= Y <= 100
2 <= M <= 100

Output Format
Print an Integer denoting answer of the calculation (x ^ y ) Mod M.

Sample TestCase 1
Input
10 2 3
Output
1
'''
def main():
    inputs = raw_input().split()
    x = int(inputs[0])
    y = int(inputs[1])
    m = int(inputs[2])
    print (x^y)%m
main()