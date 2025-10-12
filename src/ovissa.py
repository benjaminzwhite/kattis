# Óvissa
# https://open.kattis.com/problems/ovissa
# TAGS: basic
# CP4: 1.4a, One-Liner I/O
# NOTES:
"""
Wasn't 100% sure that the testcases are all made up of 'u' after reading exercise, but it seems so.
So you can just measure the length of the input string instead of counting how many 'u's.
"""
s = input()

res = s.count('u')

print(res)