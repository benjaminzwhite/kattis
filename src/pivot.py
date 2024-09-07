# Pivot
# https://open.kattis.com/problems/pivot
# TAGS: array
# CP4: 2.2b, 1D Array, Harder
# NOTES:
n = int(input())

xs = list(map(int, input().split()))

res = 0

min_to_the_r = [float('inf')] * n
max_to_the_l = [-float('inf')] * n

max_l, min_r = -float('inf'), float('inf')

for i, x in enumerate(xs):
    max_to_the_l[i] = max(max_to_the_l[i], max_l)
    max_l = max(max_l, x)

for i, x in enumerate(xs[::-1]):
    min_to_the_r[i] = min(min_to_the_r[i], min_r)
    min_r = min(min_r, x)

for l, x, r in zip(max_to_the_l, xs, min_to_the_r[::-1]):
    if l < x < r:
        res += 1

print(res)