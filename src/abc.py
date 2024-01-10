# Ants
# https://open.kattis.com/problems/ants
# TAGS: basic
# CP4: 1.4f, Function
# NOTES:
xs = sorted(map(int, input().split()))

s = input()

res = ' '.join(str(xs["ABC".index(c)]) for c in s)

print(res)