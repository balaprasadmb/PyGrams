from __future__ import print_function
import re
'''
Validate Email Address (100 Marks)
During the process of information gathering, we have to make sure that it is valid. Regex comes very handy in such tasks.
Here, we have few email addresses with us. You have to output only the valid email address.
Valid email addresses are composed of a username, domain name, and extension assembled in this format: username@domain.extension.
The username starts with an English alphabetical character, and any subsequent characters consist of one or more of the following: alphanumeric characters, -,., and _.
The domain and extension contain only English alphabetical characters.
The extension is , , or  characters in length.

Input Format
First line will contain an Integer, denoting the number of emails to validate.
Each of the next N lines will contain a string denoting the email address.

Constraints
1 <= N <= 50

Output Format
Output all the valid email address.

Sample TestCase 1
Input
2
harsh.chauhan@gmail.com
test@in
Output
harsh.chauhan@gmail.com
Explanation

test@in : Invalid Email Address

'''
def main():
    limit = int(input())
    result = []
    for _ in range(limit):
        mail = raw_input()
        if len(mail) < 50:
            if re.match(r"^[_A-Za-z0-9-\+]+(\.[_A-Za-z0-9-]+)*@" + "[A-Za-z0-9-]+(\.[A-Za-z0-9]+)*(\.[A-Za-z]{2,})$", mail) != None:
                result.append(mail)
    first = ''
    for val in result:
        print(first + val, end="")
        first = "\n"

main()