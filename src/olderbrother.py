# Older Brother
# https://open.kattis.com/problems/olderbrother
# TAGS: mathematics, number theory
# CP4: 5.3h, Working with PFs
# NOTES:
"""
It's asking "is n a prime power i.e. of the form p**k for some p and some k"

Implementation isn't optimal with the is_prime etc

CARE! Need to also check whether n itself is prime.
"""
def is_prime(n):
    return n > 1 and all(n % d != 0 for d in range(2, int(n**0.5) + 1))

# n max is 10**9 so need sqrt of this to check primes up to
# -> check to 33000
PRIMES = [x for x in range(33000) if is_prime(x)]

n = int(input())

F = 0
if is_prime(n):
    print("yes")
    F = 1
else:
    for p in PRIMES:
        if p > n:
            break
        n_ = n
        while n_ % p == 0:
            n_ //= p
        if n_ == 1:
            print("yes")
            F = 1
            break

if F == 0:
    print("no")