# Zoom
# https://open.kattis.com/problems/zoom
# TAGS: basic, array
# CP4: 1.4g, 1D Array, Easier
# NOTES:
n, k = map(int, input().split())

s = input().split()

print(*(x for i, x in enumerate(s, 1) if i % k == 0)) 