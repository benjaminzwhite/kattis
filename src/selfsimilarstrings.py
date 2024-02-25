# Self-Similar Strings
# https://open.kattis.com/problems/selfsimilarstrings
# TAGS: string, dict
# CP4: 8.7c, Fast DS+Other, Easier
# NOTES:
"""
I count all substrings of size L=1,2,.... and whenever the Counter contains a key that occurs only
once, then it violates the requirement, so answer is L-1 i.e. the last valid L is the answer.
"""
from collections import Counter

while True:
    try:
        s = input()
        for L in range(1, len(s) + 1):
            c = Counter(s[i:i + L] for i in range(len(s) - L + 1))
            if any(v == 1 for v in c.values()):
                print(L - 1)
                break
    except EOFError:
        break