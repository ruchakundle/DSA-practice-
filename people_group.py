'''
There are some groups of devils and they split into people to kill them. Devils make People them left as their group and at last the group with maximum length will be killed. Two types of devils are there namely “@” and “$”. People are represented as a string “P”

Input Format:
First line with the string for input

Output Format:
Number of groups that can be formed.

Constraints:
2<=Length of string<=10^9

Input string: PPPPPP@PPP@PP$PP
Output: 7
Explanation: 4 groups can be formed
PPPPPP@
PPP@
PP$
PP
Most people in the group lie in group 1 with 7 members.
'''


import re
s = input("enter the string : ")

groups = re.split('[@$]' , s )

c=len(groups)

print("the no. of groups formed is : " ,c)
