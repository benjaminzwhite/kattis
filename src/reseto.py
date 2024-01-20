# Reseto
# https://open.kattis.com/problems/reseto
# TAGS: mathematics
# CP4: 5.3a, Prime Numbers
# NOTES:
"""
It's a nice Sieve of Eratosthenes variant - what is the K'th number to be scratched out?

CARE! The problem starts on 2 and assumes you count the number itself.
e.g. if N = 20 and K = 3, you scratch out 2 then 4 then -> 6 <- is the K=3rd number to be crossed out
"""
N, K = map(int, input().split())
p = 2
sieve = [True] * (N + 1)

while K:
    for i, x in enumerate(sieve[p::p],1):
        if x:
            K -= 1
            if K == 0:
                print(p * i)
                break
            sieve[p * i]=False
    p += 1