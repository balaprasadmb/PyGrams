from __future__ import print_function
from collections import namedtuple
'''Collections-NamedTuple (100 Marks)
Named tuples assign meaning to each position in a tuple and allow for more readable, self-documenting code. They can be used wherever regular tuples are used, and they add the ability to access fields by name instead of position index.
You are given a data containing test results of class. The dataset consists of two columns namely : 'marks' and 'name'. These two Columns can be in any order i.e. ('name' followed by 'marks' or vice versa).
You have to find the average marks for the whole class.

Input Format
First line will contain an Integer N, denoting the number of students.
Next line will contain two string denoting the column heading.
Next N lines will contain marks and name of the students respective of column headings.

Constraints
1 <= N <= 10^3
0 <= Marks <= 100

Output Format
Output the average marks of the class rounded off to two decimal places.

Sample TestCase 1
Input
3
marks names
10 arpit
20 anushka
35 rakshita
Output
21.67
'''
def main():
    limit = input()
    columns = raw_input().split()
    stud_marks = namedtuple('Student', [columns[0],columns[1]])
    marks_sum = 0
    for _ in range(limit):
        temp = raw_input().split()
        s_record = stud_marks(marks = int(temp[0]), names = temp[1])
        marks_sum += s_record.marks
    print("%.2f" % float(float(marks_sum)/3), end='')

main()