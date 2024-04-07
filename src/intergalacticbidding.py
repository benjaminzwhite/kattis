# Intergalactic Bidding
# https://open.kattis.com/problems/intergalacticbidding
# TAGS: sorting, greedy
# CP4: 3.4c, Involving Sorting, H
# NOTES:
"""
Reading comprehension:

The values all have the property that they are <= 1/2 of the next largest, so for a given element (say of value V)
the sum of all elements smaller than it is at most V/2 + V/4 + V/8 ... <= V

-> So for each element, V, if s_remaining is >= V you must take V immediately since otherwise you cannot possibly reach s_remaining 
   even if you include all subsequent elements since their entire sum is <= V (as described above)
-> At the end of the elements, if you have decremented s_remaining to 0 then you have a solution, if not then no solution.
"""
n, s = map(int, input().split())

xs = []
for _ in range(n):
    name, val = input().split()
    xs.append((int(val), name))

xs = sorted(xs, key=lambda x: -x[0])

res = []
for x in xs:
    if x[0] > s:
        continue
    else:
        res.append(x[1])
        s -= x[0]

if s == 0:
    print(len(res))
    for x in res:
        print(x)
else:
    print(0)