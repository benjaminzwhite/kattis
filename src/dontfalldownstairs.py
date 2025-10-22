# Don't Fall Down Stairs
# https://open.kattis.com/problems/dontfalldownstairs
# TAGS: array
# CP4: 1.4m, Easy
# NOTES:
n = int(input())

xs = list(map(int, input().split()))

xs.append(0) # dummy for last element processing

res = 0
for l, r in zip(xs, xs[1:]):
    res += max(0, l - r - 1)

print(res)