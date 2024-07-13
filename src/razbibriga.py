# Razbibriga
# https://open.kattis.com/problems/razbibriga
# TAGS: mathematics, combinatorics, dict
# CP4: 0, Not In List Yet
# NOTES:
"""
I wrote a detailed solution:

https://github.com/benjaminzwhite/kattis/blob/main/detailed_solutions/razbibriga.md
"""
from itertools import product

#from string import ascii_uppercase as ALPH
ALPH = set() # optimization: only need to use all the letters that actually appear as fst,lst - might not need to take product of all 26*26*26*26

n = int(input())

d = {}
for _ in range(n):
    l = input()
    k = l[0] + l[-1]
    ALPH.add(l[0])
    ALPH.add(l[-1])
    d[k] = 1 + d.get(k, 0)

res = 0
for p in product(ALPH, repeat=4):
    N, E, S, W = p
    tmp = 1
    used = {}
    for fst, lst in [(N, E), (W, S), (N, W), (E, S)]:
        k_ = fst + lst
        tmp *= d.get(k_, 0) - used.get(k_, 0)
        used[k_] = 1 + used.get(k_, 0)
    res += tmp

print(res)