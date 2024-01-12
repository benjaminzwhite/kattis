# Recount
# https://open.kattis.com/problems/recount
# TAGS: logic
# CP4: 6.7b, Palindrome (Checking)
# NOTES:
"""
If a letter appears an odd number of times, say it forms an odd_group.

The problem is solved by removing 1 letter from each odd_group.

However, CARE! You don't need to remove the 1 letter from the "last remaining" odd_group,
because at this point the string will be itself of ODD overall length (think about it), and
therefore you can place the remaining/unpaired char in the middle of the string to form
the palindrome.

e.g. with aabbccc,  the odd_groups are {c:3}

and you don't need to remove 1 letter from the c-group because you can do e.g.:

abc|c|cba for your palindrome
"""
from collections import Counter

s = input()
c = Counter(s)

odd_groups = 0
for k, v in c.items():
    if v % 2 == 1:
        odd_groups += 1

res = max(0, odd_groups - 1) # remove a letter from all but one of the odd groups in the string

print(res)