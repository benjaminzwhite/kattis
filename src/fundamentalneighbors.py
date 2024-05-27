# Fundamental Neighbors
# https://open.kattis.com/problems/fundamentalneighbors
# TAGS: mathematics, number theory, brute force
# CP4: 5.3h, Working with PFs
# NOTES:
"""
Brute force approach passes.

Small optimization; dont have to go for the cases where n is prime since p**1 will always return 1**p = 1
"""
import sys

def solve(n):
    res = 1

    d = 2
    while d * d <= n:
        if n % d == 0:
            exp = 0
            while n % d == 0:
                n //= d
                exp += 1
            res *= (exp**d)
        d += 1
    # if n is prime then will just get p**1 so exp=1 so res *= 1; so don't need to handle this part (unlike in usual factorization where need to get p itself)
    return res

for line in sys.stdin:
    n = int(line)
    print(n, solve(n))