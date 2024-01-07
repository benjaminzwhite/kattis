# Jewelry Box
# https://open.kattis.com/problems/jewelrybox
# TAGS: mathematics
# CP4: 3.3c, Ternary Search & Others
# NOTES:
"""
- tagged as Ternary Search but can solve directly:

X = 2*h + a
Y = 2*h + b
V = h*a*b -> solve for h using above constraints
V = XYh - 2h^2 * (X+Y) + 4h^3
dV/dh = 0 -> solve quadratic to get optimal h
dV/dh = 12h^2 - 4h*(X+Y) + XY -> set to 0

need to take NEGATIVE root to get positive values for a,b,h

- left unsimplified expression for h below so can see where it comes from
"""
from math import sqrt

T = int(input())

for _ in range(T):
    X, Y = map(int, input().split())
    h = (4*(X+Y) - sqrt(16*((X+Y)**2) - 4*12*X*Y)) / 24
    a = X - 2*h
    b = Y - 2*h
    print(h*a*b)