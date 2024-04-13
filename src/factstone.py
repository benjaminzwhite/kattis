# Factstone Benchmark
# https://open.kattis.com/problems/factstone
# TAGS: mathematics
# CP4: 5.2f, Log, Exp, Pow
# NOTES:
"""
A bit overranked - basically just reading comprehension; it's just asking:
"What is largest n such that n! <= 2**bits - 1" where bits is 4 in 1960 and 2* every 10 years

log2(n!) = log2(n) + log2(n-1) + ... + log2(2) + log2(1) <= log2(2**bits - 1) < bits

so you just accumulate log2(1, 2, 3 ... k) until acc >= bits

CARE! THIS OVERSHOOTS SO RETURN k-1 AS THE VALUE WHICH DOES *NOT* OVERSHOOT
"""
from math import log2, floor

while (yr := int(input())):
    bits = 1 << (2 + floor((yr - 1960) / 10))

    rating = 1
    acc = 0
    while acc < bits:
        rating += 1
        acc += log2(rating)

    print(rating - 1) # -1 correction: need the largest value that does NOT overshoot