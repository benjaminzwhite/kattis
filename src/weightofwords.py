# The Weight Of Words
# https://open.kattis.com/problems/weightofwords
# TAGS: logic
# CP4: 3.5f, DP level 1
# NOTES:
"""
You don't need to brute force if you think about it a bit.

It's basically a "fair division" solution.
"""
from math import ceil, floor

l, w = map(int, input().split())

if ceil(w / l) < 27 and floor(w / l) > 0:
    word = (w % l) * chr(96 + ceil(w / l)) + (l - w % l) * chr(96 + floor(w / l))
    print(word)
else:
    print("impossible")