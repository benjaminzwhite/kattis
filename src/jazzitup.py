# Jazz It Up!
# https://open.kattis.com/problems/jazzitup
# TAGS: mathematics, number theory, improve
# CP4: 5.3k, Divisibility Test
# NOTES:
"""
Might not be optimal solution - TODO: IMPROVE

I find the prime factorization of n (it is said that n is SQUAREFREE so all primes are unique)
Then find the first prime that does NOT appear in prime factorization:
-> the product of n and this prime is a) greater than n and b) is also square free
"""
n = int(input())
n_ = n

prime_factors = set()

for d in range(2, n):
    if n_ % d == 0:
        n_ //= d
        prime_factors.add(d)

res = next(p for p in range(2, n) if p not in prime_factors and all(p % d != 0 for d in range(2, int(p**0.5) + 1)))

print(res)