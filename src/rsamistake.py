# RSA Mistake
# https://open.kattis.com/problems/rsamistake
# TAGS: mathematics, number theory
# CP4: 5.3h, Working with PFs
# NOTES:
from collections import defaultdict

A, B = map(int, input().split())
A_, B_ = A, B

factors = defaultdict(int)

for n in (A, B):
    d = 2
    while d * d <= n:
        if n % d == 0:
            cnt = 0
            while n % d == 0:
                cnt += 1
                n //= d
            factors[d] += cnt
        d += 1
    if n > 1:
        factors[n] += 1

if factors == {A_:1, B_:1}:
    print("full credit")
elif all(v == 1 for v in factors.values()):
    print("partial credit")
else:
    print("no credit")