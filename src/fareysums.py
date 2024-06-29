# Farey Sums
# https://open.kattis.com/problems/fareysums
# TAGS: mathematics, number theory
# CP4: 5.3e, Modified Sieve
# NOTES:
"""
I wrote a detailed solution:

https://github.com/benjaminzwhite/kattis/blob/main/detailed_solutions/fareysums.md
"""
from itertools import accumulate

def euler_phi(n):
    res = n
    for p in range(2, int(n ** 0.5) + 1):
        if n % p == 0:
            while n % p == 0:
                n //= p
            res -= res // p
    if n > 1:
        res -= res // n
    return res

# -- Precompute --
N_MAX = 10_010 # 10 is sentinel O_o
PHI = [euler_phi(x) for x in range(N_MAX)]
RES = list(accumulate(PHI))

# -- Queries --
P = int(input())
for _ in range(P):
    K, N = input().split()
    print(K, f"{3 * RES[int(N)] - 1}/2")