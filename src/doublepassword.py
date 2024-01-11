# Double Password
# https://open.kattis.com/problems/doublepassword
# TAGS: basic
# CP4: 1.4h, Easy
# NOTES:
from math import prod

s1, s2 = input(), input()

res = prod(2 if (a != b) else 1 for a, b in zip(s1, s2))

print(res)