# Bijele
# https://open.kattis.com/problems/bijele
# TAGS: basic
# CP4: 1.6b, Game (Chess)
# NOTES:
ns = map(int, input().split())

REF = (1,1,2,2,2,8)

res = (r - n for r, n in zip(REF, ns))

print(*res)