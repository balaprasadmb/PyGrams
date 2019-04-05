import sys
''' Second Highest (100 Marks)
There are a total N students present in today's class. You are given student names and their respective height (in cms).
You have to find names of all the second highest students (according to their heights).
If there are multiple students , print each name on new line.

Input Format
First line will contain an Integer N, denoting the number of students.
Next 2 * N lines contains description of each student. first line contains name of the student and second line contains height of the student.

Constraints
1 <= N <= 100

Output Format
Print name of all the students having second highest height in alphabetical order.

Sample TestCase 1
Input
4
saurabh
102
arpit
120
aditya
102
varun
101

Output
aditya
saurabh
'''
def main():
    limit = int(input())
    data_dict = {}
    for _ in range(limit):
        s_name = raw_input()
        data_dict[s_name] = input()
    max_height = max(data_dict.values())
    for key, value in list(data_dict.items()):
        if value == max_height:
            del data_dict[key]
    max_height = max(data_dict.values())
    for key in list(sorted(data_dict.keys())):
        if data_dict[key] == max_height:
            print key
main()