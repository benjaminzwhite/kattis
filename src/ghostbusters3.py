# Ghostbusters 3
# https://open.kattis.com/problems/ghostbusters3
# TAGS: mathematics, combinatorics
# CP4: 0, Not In List Yet
# NOTES:
from math import comb

BIGMOD = 10**9 + 7

n, m = map(int, input().split())
# n, m : ghost busters, ghosts

if m > n:
    # only m ghosts can get one ghostbuster each in comb(m, n) ways
    res = comb(m, n)
else:
    # assign m ghosts to n ghostbusters so that at least 1 ghostbuster per ghost
    # there are now n - m ghostbusters to multichoose from, to then assign 0 or more ghosts to
    res = comb(m + (n - m) - 1, n - m)

print(res % BIGMOD)