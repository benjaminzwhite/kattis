# Refrigerator Transport
# https://open.kattis.com/problems/refrigerator
# TAGS: brute force
# CP4: 3.2h, Math Simulation, Easier
# NOTES:
"""
- input size is so small just brute forced
"""
from math import ceil

pa, ka, pb, kb, n = map(int, input().split())

best_a, best_b = -1, -1
best_cost = float('inf')

for c_b in range(ceil(n/kb) + 1, -1, -1):
    for c_a in range(ceil(n/ka) + 1, -1, -1):
        if (c_b * kb + c_a * ka ) < n:
            break
        curr_cost = c_a * pa + c_b * pb
        if curr_cost < best_cost:
            best_cost = curr_cost
            best_a, best_b = c_a, c_b

print(best_a, best_b, best_cost)