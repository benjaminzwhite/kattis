# Apaxiaaaaaaaaaaaans!
# https://open.kattis.com/problems/apaxiaaans
# TAGS: basic
# CP4: 6.2c, Regular Expression
# NOTES:
"""
- Can solve functionally with a groupby instead of regex
"""
from itertools import groupby

s = input()

res = ''.join(k for k,_ in groupby(s))

print(res)