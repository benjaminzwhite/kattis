# Beautiful Primes
# https://open.kattis.com/problems/beautifulprimes
# TAGS: mathematics, brute force, improve
# CP4: 5.2b, Finding Formula, Harder
# NOTES:
"""
TODO: IMPROVE:

Just did brute force here using 2's and 11's (also inefficient - can avoid retaking prod each step if you want to optimize)

Try to find a formula based approach instead.
"""
from math import prod

T = int(input())
for _ in range(T):
    N = int(input())

    guess = [11] * N
    i = 0
    while len(str(prod(guess))) != N:
        guess[i] = 2
        i += 1

    print(*guess)