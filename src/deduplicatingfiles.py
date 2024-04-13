# Deduplicating Files
# https://open.kattis.com/problems/deduplicatingfiles
# TAGS: dict
# CP4: 2.3d, Hash Table (set)
# NOTES:
"""
Reading comprehension - hard to understand what exactly is being asked for:
You count +1 collision for each pair of ACTUAL ENTRIES in the input list that clash, not for each pair of "ENTRY TYPES"
For example if { hash_value==294 : a,a,a,b } then ALL 3 of the a's are counted as colliding with b (not an obvious interpretation IMHO)

So you need to count pairwise and sum if x != y
(NOTE THEREFORE YOU CAN'T DIRECTLY TAKE A SET SINCE IF SO YOU LOSE THIS "FREQUENCY" INFO
e.g. that there are 3 a's that are clashing with b rather than just 1 a)
"""
from functools import reduce
from collections import defaultdict

def hash(s):
    return reduce(lambda acc, x: acc ^ ord(x), s, 0)

while (n := int(input())):
    d = defaultdict(list)

    for _ in range(n):
        curr = input()
        d[hash(curr)].append(curr)

    uniques = 0
    collisions = 0

    for v in d.values():
        uniques += len(set(v))
        for i, x in enumerate(v):
            for y in v[i + 1:]:
                collisions += (x != y)

    print(uniques, collisions)