from __future__ import print_function
'''
Class Record (100 Marks)
You are given a dataset of N students belonging to the same class.
The data contains name of the student followed by marks they scored in five subjects which are Physics, Chemsistry, Maths, English, Hindi.
Your task is find the average marks of the class for each individual subject.

Input Format
First line will contain an Integer N, denoting  the number of students in the class.
Each of the Next N lines will contain a string S denoting the student name, followed by five integers m1, m2, m3, m4, m5 denoting the marks scored in each subject.

Constraints
1 <= N <= 10^3
1 <= S <= 10^2
0 <= m1, m2, m3, m4, m5 <= 100

Output Format
You have to print average marks upto two decimal places for each subject followed by a space. 

Sample TestCase 1
Input
2
arpit 100 75 40 56 53
anushka 100 100 76 100 100
Output
100.00 87.50 58.00 78.00 76.50

'''

def main():
    limit = int(input())
    marks_list = [0, 0, 0, 0, 0]
    for _ in range(limit):
        data_list = []
        str_data = raw_input()
        data_list = str_data.split()
        del data_list[0]
        index = 0
        for marks in data_list:
            marks_list[index] += int(marks)
            index += 1
    result_list = []
    for marks in marks_list:
        result_list.append(float(float(marks)/(100*limit)*100))
    print(" ".join(["%.2f"%item for item in result_list]), end='')

main()