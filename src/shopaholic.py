# Shopaholic
# https://open.kattis.com/problems/shopaholic
# TAGS: basic
# CP4: 3.4b, Involving Sorting, E
# NOTES:
n = int(input())

xs = map(int, input().split())

xs = sorted(xs, reverse = True)

res = sum(xs[2::3])

print(res)