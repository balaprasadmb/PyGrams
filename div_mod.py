from __future__ import print_function
''' Divmod (100 Marks)
One of the built-in functions of Python is divmod, which takes two arguments a and b and returns a tuple containing the quotient of a/b first and then the remainder a.
Your task is to read in two integers, a and b, and print divmod(a, b).

Input Format
The first line contains the first integer, a, and the second line contains the second integer, b.

Constraints
1 <= a, b <= 10^5

Output Format
Print a pair of numbers (a tuple) consisting of quotient q and remainder r.

Sample TestCase 1
Input
8
3
Output
(2, 2)
'''
def main():
    a = int(input())
    b = int(input())
    print(divmod(a, b), end='')

main()