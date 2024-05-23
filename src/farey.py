# Farey Sequence Length
# https://open.kattis.com/problems/farey
# TAGS: mathematics, number theory
# CP4: 5.3e, Modified Sieve
# NOTES:
"""
See https://en.wikipedia.org/wiki/Farey_sequence#Sequence_length_and_index_of_a_fraction

Just accumulate Euler phi totient. Initial conditions are that Farey(1) has 2 terms, then Farey(2) has Farey(1) + euler_phi(2) etc
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

RES = [None, 2]
for N in range(2, 10_005):
    RES.append(RES[-1] + euler_phi(N))

T = int(input())
for _ in range(T):
    k, n = map(int, input().split())
    print(k, RES[n])