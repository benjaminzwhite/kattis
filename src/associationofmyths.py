# Association of Myths
# https://open.kattis.com/problems/associationofmyths
# TAGS: mathematics, calculus
# CP4: 0, Not In List Yet
# NOTES:
"""
It's a troll question (?), maybe an in-joke by the author or something O_o 

Basically the final res is:

( g(n) + L )**2 / pi*e + 1 / (L + 1)

but it says g(n) is the result of taking some polynomial P and differentiating it degree(P)+1 times ; so this means that g(n) is always = 0

All the stuff about Bessel and gamma functions and erf is not needed. None of the inputs are needed either O_o
"""
from math import pi, e

a, b, c = map(float, input().split())
t1, t2, t3, t4 = map(int, input().split())
n, k, r, s, l = map(int, input().split())

res = l * l / (pi * e) + 1 / (l + 1)

print(res)