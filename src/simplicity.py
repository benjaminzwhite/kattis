# Simplicity
# https://open.kattis.com/problems/simplicity
# TAGS: greedy
# CP4: 3.4e, Non Classical, Easier
# NOTES:
from collections import Counter

s = input()

c = Counter(s)

res = 0
for _, cnt in c.most_common()[2:]:
    res += cnt

print(res)