# Divisors
# https://open.kattis.com/problems/divisors
# TAGS: mathematics, number theory, nice
# CP4: 5.3d, Prime Factors Functions
# NOTES:
"""
I wrote a detailed solution:

https://github.com/benjaminzwhite/kattis/blob/main/detailed_solutions/divisors.md
"""
import sys
from collections import defaultdict

# -- PRECOMPUTE --
def is_prime(n):
    return all(n % d > 0 for d in range(2, int(n ** 0.5) + 1))

PRIMES = [x for x in range(2, 431 + 1) if is_prime(x)]

FACTORIAL_FACTORIZATIONS = {0: defaultdict(int)}

for n in range(1, 431 + 1):
    n_ = n
    d = FACTORIAL_FACTORIZATIONS[n - 1].copy() # you just need to update the factorization of n-1! with the primes present in n itself; dont need to redo n! from scratch
    for p in PRIMES:
        while n % p == 0:
            d[p] += 1
            n //= p
    if n > 1:
        d[n] += 1
    FACTORIAL_FACTORIZATIONS[n_] = d
# -- end precompute --

# -- QUERIES --
for l in sys.stdin:
    n, k = map(int, l.split())

    res = 1
    for p, exp in FACTORIAL_FACTORIZATIONS[n].items():
        tmp = exp # these are the factors in the numerator of comb(n,k)
        tmp -= FACTORIAL_FACTORIZATIONS[k].get(p, 0)  # these are the factors in the denominator of comb(n,k) due to k!
        tmp -= FACTORIAL_FACTORIZATIONS[n-k].get(p, 0) # these are the factors in the denominator of comb(n,k) due to (n-k)!
        res *= (tmp + 1)
    
    print(res)