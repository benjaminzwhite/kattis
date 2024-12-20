# Tram
# https://open.kattis.com/problems/tram
# TAGS: mathematics, geometry, nice
# CP4: 8.7f, Geometry+Other
# NOTES:
"""
I wrote a detailed solution:

https://github.com/benjaminzwhite/kattis/blob/main/detailed_solutions/tram.md
"""
N = int(input())

res = 0
for _ in range(N):
    xi, yi = map(int, input().split())
    res += (yi - xi)

print(res / N)