# Conformity
# https://open.kattis.com/problems/conformity
# TAGS: dict
# CP4: 2.3e, Hash Table (map), E
# NOTES:
from collections import defaultdict

d = defaultdict(int)

n = int(input())

for _ in range(n):
    k = tuple(sorted(map(int, input().split()))) # NB need to sorted first then cast to tuple else sorted(tuple()) will produce a list which is unhashable
    d[k] += 1
    
max_v = -1
res = 0

# this is because there may be several keys with the SAME max_v, so need to sum total number of courses that share the max_v
# e.g. if d = { (1,2,3):5 , (2,3214):5, (983,3):3, (318,13): 2} then we sum 5+5 = 10 since 5 is the max_v and the sum of its occurences is 5 + 5 = 10
for v in d.values():
    if v > max_v:
        res = v
        max_v = v
    elif v == max_v:
        res += v

print(res)