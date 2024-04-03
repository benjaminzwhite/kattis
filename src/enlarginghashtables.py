# Enlarging Hash Tables
# https://open.kattis.com/problems/enlarginghashtables
# TAGS: mathematics, number theory
# CP4: 5.3a, Prime Numbers
# NOTES:
"""
Don't need to do anything performance related for the primes
"""
def is_prime(n):
    return n > 1 and all(n % d != 0 for d in range(2, int(n**0.5) + 1))

while True:
    n = int(input())
    if n == 0:
        break

    nn = 2 * n + 1
    while not is_prime(nn):
        nn += 1
    if is_prime(n):
        print(nn)
    else:
        print(nn, f"({n} is not prime)")