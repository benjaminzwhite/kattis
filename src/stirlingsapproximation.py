# Stirling's Approximation
# https://open.kattis.com/problems/stirlingsapproximation
# TAGS: mathematics
# CP4: 5.2f, Log, Exp, Pow
# NOTES:
"""
For performance you could precompute the accumulation of the
log(x) up to N_MAX, but not needed to get AC in this case

Also might be numerically better practice to take e.g.:
0.5 * log(2 * pi * n) 
instead of
log(sqrt(2 * pi * n))
"""
from math import e, log, pi, sqrt

while True:
    n = int(input())
    if n == 0:
        break

    numerator = sum(log(x) for x in range(1, n + 1))

    denominator = log(sqrt(2 * pi * n)) + n * log(n) - n

    print(e**(numerator - denominator))