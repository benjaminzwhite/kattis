# Catalan Numbers
# https://open.kattis.com/problems/catalan
# TAGS: mathematics, combinatorics
# CP4: 5.4c, Catalan Numbers
# NOTES:
"""
Easy with Python of course O_o
"""
from math import comb

T = int(input())

for _ in range(T):
    n = int(input())

    res = comb(2 * n, n) // (n + 1)

    print(res)