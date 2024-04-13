# Factovisors
# https://open.kattis.com/problems/factovisors
# TAGS: mathematics, number theory
# CP4: 5.3h, Working with PFs
# NOTES:
"""
Use Legendre's formula.

Implementation note:

Seems that m == 0 is a testcase input (I failed on 2nd set of testcases until I manually added m > 0 condition)
In other words, if m == 0 then we say that m DOES NOT DIVIDE n!
So basically at the print stage I check that "m > 0 and res: .... else: ..."
"""
import sys

from math import floor

def legendre_exponent(p, n):
    acc = 0
    exp = 1
    while (curr := floor(n / pow(p, exp))):
        exp += 1
        acc += curr
    return acc

for line in sys.stdin:
    n, m = map(int, line.split())
    m_copy = m

    d = 2
    factors = {}
    while d * d <= m:
        if m % d == 0:
            cnt = 0
            while m % d == 0:
                m //= d
                cnt += 1
            factors[d] = cnt
        d += 1
    if m > 1:
        factors[m] = 1

    res = all(exp <= legendre_exponent(p, n) for p, exp in factors.items())

    if m_copy > 0 and res:
        print(f"{m_copy} divides {n}!")
    else:
        print(f"{m_copy} does not divide {n}!")