# Grass Seed
# https://open.kattis.com/problems/grassseed
# TAGS: basic
# CP4: 7.2f, Quadrilaterals
# NOTES:
"""
- CARE! First Kattis problem encountered with FLOATS in inputs rather than ints
"""
C = float(input())
L = int(input())
res = 0

for _ in range(L):
    w, h = map(float, input().split())
    res += w * h

print(C * res)