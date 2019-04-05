from __future__ import print_function
import re
'''
Validate Phone Numbers (100 Marks)
In the country of Utopia, Phones Numbers starts with the digit 1 or 2 followed by exactly 12 digits i.e Phones Numbers comprises of 13 digits.
Now, Given N numbers you have to check, whether they are Valid or Invalid.
If they are Valid, print Valid" otherwise print "Invalid".

Input Format
First Line will contain an Integer, denoting the count of phone numbers.
Each of the Next N lines, contains a Phone Number.

Constraints
1 <= N <= 10^3

Output Format
For each Phone Number, print "Valid" or "Invalid" in a new line.

Sample TestCase 1
Input
2
1123456789123
0112345678912
Output
Valid
Invalid
'''
def main():
    limit = int(input())
    result = []
    for _ in range(limit):
        numbs = raw_input()
        if len(numbs) == 13:
            if re.match(r'^[1, 2]\d{12}$', numbs) != None:
                result.append("Valid")
            else:
                result.append("Invalid")
        else:
            result.append("Invalid")
    first = ''
    for val in result:
        print(first + val, end="")
        first = "\n"

main()
