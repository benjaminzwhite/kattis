# BizzFuzz
# https://open.kattis.com/problems/bizzfuzz
# TAGS: mathematics, number theory
# CP4: 0, Not In List Yet
# NOTES:
"""
Kattis Python 3.8 so doesn't have math.lcm yet O_o
"""
from math import gcd

def upto(n, c, d):
    return n * gcd(c, d) // (c * d)
 
a, b, c, d = map(int, input().split())

print(upto(b, c, d) - upto(a - 1, c, d))