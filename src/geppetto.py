# Geppetto
# https://open.kattis.com/problems/geppetto
# TAGS: brute force, mathematics, combinatorics, improve
# CP4: 3.2f, Iterative (Combination)
# NOTES:
"""
TODO: IMPROVE: Did brute force, can probably do PIE counting but need to handle the double counting:

Basically, good sets are 2**N, then there you remove ONES * 2**(N-2) "bad" subsets which contain one of the pairs,
but then when you add back TWOS... you have to consider that some 2-pairs may overlap to form 3-element sets eg. {1,2} {2,3}
"""
from itertools import combinations

N, M = map(int, input().split())

xs = set()
for _ in range(M):
    a, b = map(int, input().split())
    a, b = min(a, b), max(a, b) # need to ensure that e.g. if (2,5) and (5,2) are both in inputs that only one gets added since they are the same as a pair -> so only add tuples where a<b
    xs.add((a, b))

cnt = 2 ** N
for r in range(2, N + 1):
    for c in combinations(range(1, N + 1), r):
        if any(a in c and b in c for a, b in xs):
            cnt -= 1

print(cnt)