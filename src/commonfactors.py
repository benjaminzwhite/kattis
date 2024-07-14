# Common Factors
# https://open.kattis.com/problems/commonfactors
# TAGS: mathematics, number theory
# CP4: 0, Not In List Yet
# NOTES:
"""
I wrote a detailed solution:

https://github.com/benjaminzwhite/kattis/blob/main/detailed_solutions/commonfactors.md
"""
from math import gcd

# -- Precompute --
N_MAX = 10**18
SIEVE_MAX = 54 # generates first 54 primes: this is so that product of all of them is > 10**18 for the first time
SIEVE = [True] * SIEVE_MAX
SIEVE[0] = False
SIEVE[1] = False
PRIMES = []
for d in range(2, SIEVE_MAX):
    if SIEVE[d]:
        PRIMES.append(d)
        SIEVE[d * d::d] = [False] * ((SIEVE_MAX - d * d - 1) // d + 1)

# -- Query --
target_n = int(input())

curr_prod = 1
euler_phi_acc = 1
for p in PRIMES:
    if curr_prod * p > target_n:
        break
    else:
        curr_prod *= p
        euler_phi_acc *= (p - 1)

res_numerator = curr_prod - euler_phi_acc

g = gcd(res_numerator, curr_prod)

print(f"{res_numerator // g}/{curr_prod // g}")