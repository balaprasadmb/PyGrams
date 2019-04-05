from __future__ import print_function
import numpy as np
'''
 Identity Matrix (100 Marks)
Numpy Package contains an inbuilt tool named identity
The identity tool returns an identity array. An identity array is a square matrix with all the main diagonal elements as 1 and the rest as 0.
You have to print a numpy array(square matrix of size N*N) consisting of integers with diagonal elements as 1 and rest as 0.

Input Format
First and only line of input contains an Integer N.

Constraints
2 <= N <= 100

Output Format
Output a Identity Matrix of Size N*N.

Sample TestCase 1
Input
3
Output
[[1 0 0]
[0 1 0]
[0 0 1]]
'''
def main():
    limit = int(input())
    print(np.identity(limit, int), end="")

main()