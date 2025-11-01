# Trojke
# https://open.kattis.com/problems/trojke
# TAGS: brute force, mathematics
# CP4: 7.2b, Lines
# NOTES:
"""
Brute force try all 3 points combinations and check that they have same gradient
"""
from itertools import combinations

n = int(input())

pts = []
for row in range(n):
    for col, cell in enumerate(input()):
        if cell.isalpha():
            pts.append((row, col)) 

res = 0
for (x1, y1), (x2, y2), (x3, y3) in combinations(pts, 3):
    if (y2 - y1) * (x3 - x2) == (y3 - y2) * (x2 - x1):
        res += 1

print(res)