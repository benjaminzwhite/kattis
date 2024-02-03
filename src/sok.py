# Sok
# https://open.kattis.com/problems/sok
# TAGS: basic
# CP4: 1.4i, Still Easy
# NOTES:
a, b, c = map(int, input().split())

i, j, k = map(int, input().split())

ra, rb, rc = a / i, b / j, c / k

r = min(ra, rb, rc)

print(a - r * i, b - r * j, c - r * k)