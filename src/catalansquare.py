# Catalan Square
# https://open.kattis.com/problems/catalansquare
# TAGS: mathematics, combinatorics, proof
# CP4: 5.4c, Catalan Numbers
# NOTES:
"""
From reading the footnote:

if p(x) = sum a_n x**n and q(x) = sum b_n x**n, then p(x) . q(x) (where . is the Cauchy product of power series) is

p(x) . q(x) = sum z_n x**n 

where z_n = SUM a_k b_n-k <- so in otherwords with p and q the catalan series, we get that z_n will itself satisfy the Catalan recurrence.
"""
from math import comb

n = int(input())

res = comb(2 * (n + 1), (n + 1)) // ((n + 1) + 1)

print(res)