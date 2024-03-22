# Relatives
# https://open.kattis.com/problems/relatives
# TAGS: mathematics, number theory
# CP4: 5.3d, Prime Factors Functions
# NOTES:
"""
Just count relatively prime numbers to n, Euler phi
"""
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

while True:
    n = int(input())
    if n == 0:
        break
    else:
        print(euler_phi(n))