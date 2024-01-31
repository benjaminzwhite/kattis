# Falling Apart
# https://open.kattis.com/problems/fallingapart
# TAGS: sorting, greedy
# CP4: 3.4b, Involving Sorting, E
# NOTES:
n = input()

xs = sorted(map(int, input().split()), reverse=True)

A = sum(xs[::2])
B = sum(xs[1::2])

print(A, B)