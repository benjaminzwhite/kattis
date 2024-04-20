# Subprime
# https://open.kattis.com/problems/subprime
# TAGS: mathematics, number theory, brute force
# CP4: 0, Not In List Yet
# NOTES:
SIEVE_MAX = 1_500_000 # generates first 114156 primes (you need 100_000 primes)

PRIMES = [-1] # queries are 1-based indexed so init with dummy element

SIEVE = [True] * SIEVE_MAX
SIEVE[0] = False
SIEVE[1] = False
for d in range(2, SIEVE_MAX):
    if SIEVE[d]:
        PRIMES.append(str(d)) # CARE! cast d to string
        SIEVE[d * d::d] = [False] * ((SIEVE_MAX - d * d - 1) // d + 1)

l, h = map(int, input().split())
p = input()

res = sum(1 for n in PRIMES[l:h + 1] if p in n) # brute force

print(res)