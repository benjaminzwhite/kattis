# Töflur
# https://open.kattis.com/problems/toflur
# TAGS: sorting, greedy
# CP4: 3.4b, Involving Sorting, E
# NOTES:
n = int(input())

xs = sorted(map(int, input().split()))

res = sum((b - a)**2 for a, b in zip(xs, xs[1:]))

print(res)