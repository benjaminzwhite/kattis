# Happy and Unhappy Numbers
# https://open.kattis.com/problems/happyandunhappynumbers
# TAGS: mathematics, number theory, range sum, nice
# CP4: 0, Not In List Yet
# NOTES:
"""
I wrote a detailed solution:

https://github.com/benjaminzwhite/kattis/blob/main/detailed_solutions/happyandunhappynumbers.md

Note: there are 2 different ways of solving there, here I am only saving one of them
"""
from itertools import permutations

N_MAX = 1_000_050
H = [-1] * N_MAX

def is_happy(x):
    if H[x] > -1:
        return H[x]

    seen = set()

    while True:
        if H[x] == 1 or x == 1:
            for y in seen:
                for p in permutations(str(y)):
                    tmp = int(''.join(p))
                    if tmp < N_MAX:
                        H[tmp] = 1
            H[x] = 1
            return 1
        elif H[x] == 0 or x in seen:
            for z in seen:
                for p in permutations(str(z)):
                    tmp = int(''.join(p))
                    if tmp < N_MAX:
                        H[tmp] = 0
            return 0
        seen.add(x)
        x = sum(d**2 for d in map(int, str(x)))

RES = [0] * N_MAX
for n in range(1, N_MAX):
    RES[n] = RES[n - 1] + is_happy(n)

T = int(input())
for _ in range(T):
    l, r = map(int, input().split())
    print(RES[r] - RES[l - 1]) # CARE! -1 due to taking INCLUSIVE range sum