# An Industrial Spy
# https://open.kattis.com/problems/industrialspy
# TAGS: mathematics, number theory, sieve, improve
# CP4: 8.7h, Mathematics+Other
# NOTES:
"""
TODO: IMPROVE - practice solve with bitmask in another language without using permutations itertools

Brute force passes within the 2 seconds time limit in Python 3

YOU *CANNOT* do sum(PRIMES[n] for n in perms(x,k)) FOR EACH k INCREMENTALLY BECAUSE IT IS
POSSIBLE THAT some larger k value will lead to DOUBLE COUNTING SOME VALUES OF n

e.g. with the testcase 011 ->
k=2 perms are 01,11,10.. etc and
k=3 perms are ...110, 011 <== CARE! NOTE 011 k=3 will int() to 11 SO YOU WILL DOUBLE COUNT IT 
"""
from itertools import permutations

# -- Precompute primes --
N_MAX = 10**7
PRIMES = [True] * N_MAX
PRIMES[0] = False
PRIMES[1] = False
d = 2
while d * d <= N_MAX:
    if PRIMES[d]:
        PRIMES[2 * d::d] = [False] * ((N_MAX - 2 * d - 1) // d + 1)
    d += 1

# -- Queries --
T = int(input())

for _ in range(T):
    x = input()
    
    tmp = []
    for k in range(1, len(x) + 1):
        tmp.extend(list(map(int, map(''.join, permutations(x, k)))))
    
    res = sum(PRIMES[n] for n in set(tmp))
    print(res)