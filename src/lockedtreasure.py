# Locked Treasure
# https://open.kattis.com/problems/lockedtreasure
# TAGS: mathematics, combinatorics
# CP4: 5.4b, Binomial Coefficients
# NOTES:
from math import comb

T = int(input())

for _ in range(T):
    n, m = map(int, input().split())
    print(comb(n, m - 1))