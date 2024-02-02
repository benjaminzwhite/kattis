# Akcija
# https://open.kattis.com/problems/akcija
# TAGS: sorting, greedy
# CP4: 3.4b, Involving Sorting, E
# NOTES:
n = int(input())

xs = [int(input()) for _ in range(n)]
xs = sorted(xs, reverse=True)

res = sum(xs) - sum(xs[2::3])

print(res)