# The Trip, 2007
# https://open.kattis.com/problems/trip2007
# TAGS: sorting, greedy
# CP4: 3.4c, Involving Sorting, H
# NOTES:
from collections import Counter

first_test_case = True

while (n := int(input())):
    if not first_test_case:
        print()
    first_test_case = False

    xs = list(map(int, input().split())) # update: don't reuse xs so don't need to list()
    c = Counter(xs)
    K = sorted(c.keys(), reverse=True)

    res = []
    while n:
        tmp = []
        for k in K:
            if c[k] > 0:
                tmp.append(k)
                c[k] -= 1
                n -= 1
        res.append(tmp)
    
    print(len(res))
    for x in res:
        print(*x)