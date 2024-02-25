# Secret Santa
# https://open.kattis.com/problems/secretsanta
# TAGS: mathematics, combinatorics
# CP4: 5.5a, Probability, Easier
# NOTES:
"""
The answer is given by the derangement formula, sometimes written as: !n

The standard result is that !n -> 1/e for large n.

Since input n goes to 10**12 you can't compute it via factorial - instead you note that the 1/e approximation to !n (derangements)
is very good already for n=10 approx.

Exercise wants agreement to 6 decimal places so found experimentally that n=20 passes and doesn't TLE with factorial calculations.
"""
from math import factorial, e

n = int(input())

if n > 20:
    print(1 - 1 / e)
else:
    print(1 - sum((-1)**i / factorial(i) for i in range(n + 1)))