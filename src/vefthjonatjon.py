# Vefþjónatjón
# https://open.kattis.com/problems/vefthjonatjon
# TAGS: basic, array
# CP4: 1.4k, 1D Array, Easier
# NOTES:
n = int(input())

xs = []
for _ in range(n):
    xs.append(input().split())

res = float('inf')
for col in zip(*xs):
    res = min(res, col.count('J'))

print(res)