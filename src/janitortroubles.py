# Janitor Troubles
# https://open.kattis.com/problems/janitortroubles
# TAGS: mathematics, geometry
# CP4: 9.form, Formulas/Theorems
# NOTES:
"""
https://en.wikipedia.org/wiki/Bretschneider%27s_formula

max is then:

Brahmagupta formula
"""
from math import sqrt

a, b, c, d = map(int, input().split())

s = (a + b + c + d) / 2

print(sqrt((s - a) * (s - b) * (s - c) * (s - d)))