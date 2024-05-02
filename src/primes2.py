# Blackboard Numbers
# https://open.kattis.com/problems/primes2
# TAGS: mathematics, number theory
# CP4: 5.3b, (Prob) Prime Testing
# NOTES:
"""
Don't need performant is_prime()
"""
from math import gcd

def is_prime(n):
    return n > 1 and all(n % d != 0 for d in range(2, int(n**0.5) + 1))

T = int(input())
for _ in range(T):
    s = input()

    num, denom = 0, 0
    for base in (2, 8, 10, 16):
        try:
            n = int(s, base)
            denom += 1
            if is_prime(n):
                num += 1
        except:
            continue


    g = gcd(num, denom)
    print(f"{num // g}/{denom // g}")