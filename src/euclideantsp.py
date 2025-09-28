# Euclidean TSP
# https://open.kattis.com/problems/euclideantsp
# TAGS: ternary search
# CP4: 3.3c, Ternary Search & Others
# NOTES:
"""
It's mainly reading comprehension: after submission I noticed that you don't need to compare f(c1) vs f(c2)
in the ternary search part, since the function depends on a bunch of constants that will cancel out, and is
unimodal so I think you can just compare c1 and c2 directly - this avoids having to calculate a bunch of
large (possibly overflowing) numbers.

Also I currently set the "lo" value to 1e-3 instead of 0 to avoid division by 0 but again I think this would
be avoidable if you don't calculate f() during the ternary search.
"""
from math import log2, sqrt, log, exp

def f(c):
    t1 = (n * log2(n) ** (c * sqrt(2))) / (p * 10 ** 9)
    t2 = s * (1 + 1 / c) / v

    return t1 + t2

n, p, s, v = map(float, input().split())

lo = 1e-3 # c can't be exactly zero else divide by zero in formula?
hi = 150 # overflows around 440 (UPDATE: I think you should solve by not comparing f(c1) < f(c2) see notes)

for _ in range(100):
    delta = (hi - lo) / 3
    c1 = lo + delta
    c2 = hi - delta

    # UPDATE: here I think you can just compare c1 < c2 and avoid the large numbers in f(c1) and f(c2) calculation
    if f(c1) < f(c2):
        hi = c2
    else:
        lo = c1

print(f(lo), lo)