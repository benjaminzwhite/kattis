# Veci
# https://open.kattis.com/problems/veci
# TAGS: brute force, mathematics, combinatorics
# CP4: 3.2e, Iterative (Permutation)
# NOTES:
from itertools import permutations

s = input()
n = int(s)
res = float('inf')

for p in permutations(s):
    if (tmp := int(''.join(p))) > n:
        res = min(res, tmp)
        
if res != float('inf'):
    print(res)
else:
    print(0)