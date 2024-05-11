# Pea Pattern
# https://open.kattis.com/problems/peapattern
# TAGS: string, dict
# CP4: 0, Not In List Yet
# NOTES:
"""
Just do as asked

They say that they believe all inputs have answer within 100 rounds but if you find one that
doesn't, print "I’m bored." but this doesn't appear in the testcases it seems.
"""
from collections import Counter

n, m = input().split()

res = 1
for _ in range(100):
    if n == m:
        break
    res += 1
    c = Counter(n)
    n = ''.join(str(v) + k for k, v in sorted(c.items()))

if res <= 100:
    print(res)
else:
    print("Does not appear")