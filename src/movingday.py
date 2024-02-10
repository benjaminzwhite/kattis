# Moving Day
# https://open.kattis.com/problems/movingday
# TAGS: basic, geometry
# CP4: 7.4a, 3D Geometry
# NOTES:
n, V = map(int, input().split())

max_vol = -float('inf')

for _ in range(n):
    l, w, h = map(int, input().split())
    v = l * w * h
    max_vol = max(max_vol, v)
    
print(max_vol - V)