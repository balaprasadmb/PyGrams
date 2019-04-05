'''
For the sake of the problem assume the river is flowing from left to right and Bob is currently sitting at x-coordinate = 0 (origin). All the fishes
are swimming with the river's flow at a uniform speed of 1 from left to right. The x-coordinates increases as we move rightwards in the river and decreases
as we move leftwards. Initially all the fishes has non-positive x-coordinates.

    You are given the information about N salmons in two arrays len and time, where 
len[i] = length of the ith salmon and time[i] = time at which the head of the ith salmon reaches the x-coordinate = 0 (origin).
So, at any time T, the ith salmon  has its head at x-coordinate = T - time[i] and tail at x-coordinate = T - time[i] - len[i].

At any point of time Bob can catch all the salmons whose any part of body (between head and tail, both inclusive) is at origin.
Bob wants to catch salmons no more than twice. What is the maximum number of Salmons Bob can catch?

    Input Format
First line of input contains an integer N representing the number of salmons.
Second line of input contains N space separated integers representing the contents of array len.
Third line of input contains N space separated integers representing the contents of array time.
The last line of input is kept blank.

    Constraints
1 <= N <= 1000
1 <= len[i] <= 1000, 000, 000
0 <= time[i] <= 1000, 000, 000

    Output Format
An integer representing the maximum number of salmons Bob can catch.

   Sample TestCase 1
Input
5
2 4 4 2 4
1 4 1 6 4

Output
5

    Sample TestCase 2
Input
1
1
2

Output
1

'''
def fish_cather():
    n = int(input())
    l = []
    for i in range(n):
        l.append([])
        




        