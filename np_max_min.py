from __future__ import print_function
import numpy as np
'''
 Max of Min (100 Marks)
You will be given a 2-Dimensional Matrix of size NxM.
By using Inbuilt Max and Min function present in NumPy Package, You have to perform the min function over axis = 0 and then find the max of that.

Input Format
First line contains two integers N and M, denoting the size of the Matrix.
Next N lines contains M integers.

Constraints
2 <= N <= 100
2 <= M <= 100

Output Format
You have to print an Integer denoting the answer i.e  maximum over minimum(axis = 0).

Sample TestCase 1
Input
4 2
1 4
4 6
3 7
4 5
Output
4
'''
def main():
    inputs = [int(x) for x in raw_input().split()]
    mat = []
    for _ in range(inputs[0]):
        t = [int(x) for x in raw_input().split()]
        mat.append(t)
    print(max(np.min(mat, 0)), end="")

main()