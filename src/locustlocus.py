# Locust Locus
# https://open.kattis.com/problems/locustlocus
# TAGS: mathematics
# CP4: 5.3f, GCD and/or LCM
# NOTES:
"""
Implementation note: math.lcm is NOT AVAILABLE on Kattis 3.8 since it was added in Python 3.9 O_o
"""
from math import gcd

T = int(input())

best = 10**9

for _ in range(T):
    l = input()
    y, a, b = map(int, l.split())
    res = y + (a * b) // gcd(a, b)
    if res < best:
        best = res

print(best)