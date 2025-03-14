# Factorial Power
# https://open.kattis.com/problems/factorialpower
# TAGS: mathematics, number theory, nice
# CP4: 0, Not In List Yet
# NOTES:
"""
I wrote a detailed solution:

https://github.com/benjaminzwhite/kattis/blob/main/detailed_solutions/factorialpower.md
"""
from math import floor

n, m = map(int, input().split())

# CARE! store the original input for later, as we will modify n while getting its prime factorization
n_orig = n

# -- Get prime factorization of n --
factors = {}
d = 2
while d * d <= n:
    exponent = 0
    while n % d == 0:
        n //= d
        exponent += 1
    if exponent > 0:
        factors[d] = exponent
    d += 1
if n > 1:
    if n not in factors:
        factors[n] = 0
    factors[n] += 1

# -- Apply Legendre's formula to the known primes that appear in n (see Implementation note above) --
legendre = {}
for p in factors:
    exponent = 0
    k = 1
    while True:
        curr = floor(m / pow(p, k))
        if curr == 0:
            break
        exponent += curr
        k += 1
    legendre[p] = exponent

# -- The result is the min ratio between exponents across the factors of n --
largest_k = float('inf')
for prime, exponent in factors.items():
	largest_k = min(largest_k, floor(legendre[prime] / exponent))

print(largest_k)