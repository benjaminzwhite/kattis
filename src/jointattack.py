# Joint Attack
# https://open.kattis.com/problems/jointattack
# TAGS: mathematics, number theory
# CP4: 5.2i, Fractions
# NOTES:
"""
Continued fractions - easy with Python Fraction
"""
from fractions import Fraction

n = int(input())
xs = list(map(int, input().split()))

xs = xs[::-1]

curr = Fraction(xs[0], 1)

for x in xs[1:]:
    curr = 1 / curr
    curr += Fraction(x, 1)

print(curr)