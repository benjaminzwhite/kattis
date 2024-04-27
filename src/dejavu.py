# Dejavu
# https://open.kattis.com/problems/dejavu
# TAGS: mathematics, geometry, combinatorics
# CP4: 8.7f, Geometry+Other
# NOTES:
"""
For each point, check how many times it occurs as the right angle of some triangle using 2 other points

NOTE: since only asks for those right triangles with legs parallel to coordinate axes this is easy since 
you just count points sharing x coord and points sharing y coord
i.e. how many OTHER times x coord appears and same for y coord
"""
from collections import defaultdict

N = int(input())

ps = []
d_x = defaultdict(int)
d_y = defaultdict(int)
for _ in range(N):
    x, y = map(int, input().split())
    ps.append((x, y))
    d_x[x] += 1
    d_y[y] += 1

cnt = 0
for x, y in ps:
    cnt += (d_x[x] - 1) * (d_y[y] - 1)

print(cnt)