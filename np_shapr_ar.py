from __future__ import print_function
import numpy as np
'''Reshape The Array (100 Marks)
The shape tool gives a tuple of array dimensions and can be used to change the dimensions of an array. 
The reshape tool gives a new shape to an array without changing its data. It creates a new array and does not modify the original array itself.
Now, Given 9 Integers, You have to convert them into 3*3 Numpy array using Reshape function.

Input Format
Single line containing 9 space separated integers.

Constraints
1 <= Integers <= 100

Output Format
Output 3*3 Numpy Array.

Sample TestCase 1
Input
1 2 3 4 5 6 7 8 9
Output
[[1 2 3]
[4 5 6]
[7 8 9]]
'''
def main():
    mat = [int(x) for x in raw_input().split()]
    mat = np.reshape(mat, (3, 3))
    print(mat, end="")

main()