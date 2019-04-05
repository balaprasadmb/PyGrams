from __future__ import print_function
import numpy as np
'''
 Determinant Of A Matrix (100 Marks)
Determinant is a very useful value in linear algebra. It calculated from the diagonal elements of a square matrix.
The NumPy module also comes with a number of built-in routines for linear algebra calculations. 
The numpy.linalg.det() function calculates the determinant of the input matrix.
Now, Given a square matrix calculate and output the determinant of the matrix.

Input Format
First line will contain an Integer N, denoting the size of square matrix.
Each of the next N lines contains N Integers denoting the elements of the matrix.

Constraints
2 <= N <= 20

Output Format
Output a number upto 1 decimal place denoting the determinant of the Matrix.

Sample TestCase 1
Input
2
4 3
2 1
Output
-2.0
'''
def main():
    limit = int(input())
    mat = []
    for _ in range(limit):
        t = [int(x) for x in raw_input().split()]
        mat.append(t)
    print(np.linalg.det(mat), end="")

main()