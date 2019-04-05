import itertools
'''
Cartesian Product (100 Marks)
For sets A and B, the Cartesian product of A and B, denoted AxB, is the set of all ordered pairs (a, b) such that a A and b B. That is, AxB = {(a, b)| a A b B}. 
itertools.product() computes the cartesian product of input iterables. 
 For example, product(P, Q) returns the same as ((x,y) for x in P for y in Q). 
You are given a two lists A and B. Your task is to compute their cartesian product AXB.

Input Format
The first line contains the space separated elements of list. 
The second line contains the space separated elements of list.
Both lists have no duplicate integer elements.

Constraints
1 <= elements in List A <= 40
1 <= elements in List B <= 40

Output Format
Output the cartesian product of the two list as tuples separated by spaces.

Sample TestCase 1
Input
2 4
7 8
Output
(2, 7) (2, 8) (2, 9) (4, 7) (4, 8) (4, 9)

'''
def main():
    set1 = set(int(x) for x in raw_input().split())
    set2 = set(int(y) for y in raw_input().split())
    for i in itertools.product(set1, sorted(set2)):
        print i,

main()
