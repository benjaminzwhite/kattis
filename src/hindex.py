# H-Index
# https://open.kattis.com/problems/hindex
# TAGS: array, sorting
# CP4: 3.3b, Bisection and BSTA, E
# NOTES:
"""
- Unoptimized; for ex could break early once you find x < i since all subsequent xx will also be < ii
"""
n = int(input())

xs = []
for _ in range(n):
	xs.append(int(input()))

xs = sorted(xs, reverse=True)

res = max((i for i, x in enumerate(xs, 1) if x >= i), default=0)

print(res)