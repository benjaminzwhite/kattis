# Aldursröðun
# https://open.kattis.com/problems/aldursrodun
# TAGS: mathematics, combinatorics
# CP4: 3.2f, Iterative (Permutation)
# NOTES:
from itertools import permutations
from math import gcd

n = int(input())

xs = list(map(int, input().split()))

flg = True
for perm in permutations(xs):
    if all(gcd(l, r) > 1 for l, r in zip(perm, perm[1:])):
        print(*perm)
        flg = False
        break

if flg:
    print("Neibb")