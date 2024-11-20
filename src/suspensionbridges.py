# Suspension Bridges
# https://open.kattis.com/problems/suspensionbridges
# TAGS: binary search, mathematics, calculus
# CP4: 3.3b, Bisection and BSTA, E
# NOTES:
"""
Just have to mess around with the "epsilon"/numerical precision values until it is AC
(I don't see how to rewrite stuff to avoid the hyperbolic sinh/cosh functions or exponentials)
"""
from math import cosh, sinh

d, s = map(int, input().split())

l, r = 0, 1e9
a = 1e9

while abs((a + s) - a * cosh(d / (2 * a))) > (1 / (10**6)):
    a = (l + r) / 2
    if (a + s) < a * cosh(d / (2 * a)):
        l = a
    else:
        r = a
        
res = 2 * a * sinh(d / (2 * a))

print(res)