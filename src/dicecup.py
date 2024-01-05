# Dice Cup
# https://open.kattis.com/problems/dicecup
# TAGS: basic
# CP4: 3.2h, Math Simulation, Easier
# NOTES:
"""
- CARE! input N, M are NOT always such that N < M
"""
N, M = map(int, input().split())

N, M = min(N,M), max(N,M)

for s in range(N, M+1):
    print(s+1)