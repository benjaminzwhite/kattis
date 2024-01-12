# Pizza Crust
# https://open.kattis.com/problems/pizza2
# TAGS: basic
# CP4: 7.2c, Circles
# NOTES:
r, c = map(int, input().split())

print((10 * (r - c) / r)**2)