'''
Decompress String (100 Marks)
You are given a string S. You to have to first sort the characters in the string. Now, Suppose a character 'c' occurs x times in the  modified string. 
Replace these consecutive occurrences of the character 'c' with (x, c) in the string.
Itertools.groupby() will help you in achieving it.

Input Format
First line will contain a string s.

Constraints
2 <= |s| <= 10^3

Output Format
A single line containing the modified string. 

Sample TestCase 1
Input
aaabbcccd
Output
(3, 'a') (2, 'b') (3, 'c') (1, 'd')
'''
def main():
    input_str = raw_input()
    data_dict = {}
    for char in input_str:
        if char in data_dict:
            data_dict[char] += 1
        else:
            data_dict[char] = 1
    for key, val in list(data_dict.items()):
        print (val, key),
main()