# Clock Construction
# https://open.kattis.com/problems/clockconstruction
# TAGS: logic, array, nice
# CP4: 8.7d, Fast DS+Other, Harder
# NOTES:
"""
I wrote a detailed solution:

https://github.com/benjaminzwhite/kattis/blob/main/detailed_solutions/clockconstruction.md
"""
N, H, W = map(int, input().split())

flattened_pictures = []
for _ in range(N * H):
    flattened_pictures.extend(input())

# the patterns now are the "period W * H" string slices in the flattened_pictures
patterns = [tuple(flattened_pictures[i::W * H]) for i in range(W * H)]

# take the set() to get the number of distinct groups
print(len(set(patterns)))