# Yoda
# https://open.kattis.com/problems/yoda
# TAGS: array
# CP4: 5.2j, Really Ad Hoc
# NOTES:
"""
itertools zip_longest with fillvalue 0 makes it easy to implement the logic
"""
from itertools import zip_longest

s1 = input()
s2 = input()

upper = []
lower = []

for u, l in zip_longest(map(int, s1[::-1]), map(int, s2[::-1]), fillvalue=0):
    if u == l:
        upper.append(u)
        lower.append(l)
    elif u > l:
        upper.append(u)
    else:
        lower.append(l)

for arr in (upper, lower):
    if arr:
        print(int(''.join(map(str, arr[::-1]))))
    else:
        print("YODA")