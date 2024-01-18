# Prsteni
# https://open.kattis.com/problems/prsteni
# TAGS: basic, mathematics
# CP4: 5.3f, GCD and/or LCM
# NOTES:
from fractions import Fraction

N = int(input())

radii = list(map(int, input().split()))

for r in radii[1:]:
    frac = Fraction(radii[0], r)
    print(f"{frac.numerator}/{frac.denominator}")