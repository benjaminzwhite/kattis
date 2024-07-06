# Groupthink
# https://open.kattis.com/problems/groupthink
# TAGS: mathematics, improve
# CP4: 0, Not In List Yet
# NOTES:
"""
TODO: IMPROVE: Not the best implementation - it's just "do as you are told", checking 3 properties.
Maybe can simplify to make it cleaner.

---

Implementation note:

Need to use combinations_with_replacement rather than just combinations because it has testcases with n < 3
i.e. only 1 or 2 elements, so in such cases combinations(ELEMENTS, 3) won't produce an iterable
(in such cases you are actually doing stuff like (x * x) * x = x * (x * x) "trivial checks")
"""
from itertools import combinations_with_replacement

n = int(input())

d = {}
for _ in range(n * n):
    i, j, k = input().split()
    d[(i, j)] = k

ELEMENTS = list(map(str, range(n)))

# p1
p1flg = True
for x, y, z in combinations_with_replacement(ELEMENTS, 3):
    if d[ (d[(x,y)], z)] != d[ (x, d[(y, z)])]:
        p1flg = False
        break

# p2
p2flg = False
for I_candidate in ELEMENTS:
    if all(d[(x, I_candidate)] == d[(I_candidate, x)] == x for x in ELEMENTS):
        p2flg = True
        I = I_candidate
        break

# p3
p3flg = True
if p2flg:
    for x in ELEMENTS:
        if not any(d[(x, x_)] == d[(x_, x)] == I for x_ in ELEMENTS):
            p3flg = False
            break


if p1flg and p2flg and p3flg:
    print("group")
elif p1flg and p2flg:
    print("monoid")
elif p1flg:
    print("semigroup")
else:
    print("magma")