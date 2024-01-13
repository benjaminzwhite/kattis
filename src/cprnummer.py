# CPR Number
# https://open.kattis.com/problems/cprnummer
# TAGS: basic
# CP4: 1.6e, Real Life, Easier
# NOTES:
REF = (4, 3, 2, 7, 6, 5, 4, 3, 2, 1)

s = input()

xs = map(int, filter(lambda x: x != '-', s))

res = sum(ref * x for ref, x in zip(REF, xs))

print(int(res % 11 == 0))