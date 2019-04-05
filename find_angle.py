import math
from __future__ import print_function
'''Find Angle (100 Marks)
Given a right angled triangle ABC, right angled at B. Find angle ABD, where D is the mid-point of the hypotenuse(side AC).
You will be given two integers denoting sides AB and BC respectively.
Round off your answer to the nearest Integer.

Input Format
First line will contain an Integer denoting side AB.
Second line will contain an Integer denoting side BC.


Constraints
1 <= side AB <= 200
1 <= side BC <= 200

Output Format
Output Angle ABD, rounded off to nearest integer.

Sample TestCase 1
Input
6
6
Output
45
'''
def main():
    ab = float(input())
    bc = float(input())
    print(int(round(math.degrees(math.atan(bc/ab)))), end='')