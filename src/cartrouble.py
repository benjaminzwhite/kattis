# Car Trouble
# https://open.kattis.com/problems/cartrouble
# TAGS: DFS
# CP4: 4.2a, Finding CCs
# NOTES:
"""
This is way overranked, it's just DFS but with artificial difficulties:
- unclear explanations (you have to read the input section to determine that the "outer road" always has id = 0)
- inputs aren't in order and can skip IDs
- weird output requirements
- have to track input order etc.
"""
from collections import defaultdict

streets = int(input())

from_d, to_d = defaultdict(list), defaultdict(list)

input_order = []
all_ok = True

for _ in range(streets):
    start, _, *xs = input().split()
    input_order.append(start)
    for x in xs:
        from_d[start].append(x)
        to_d[x].append(start)

stk1 = ['0']
reachable1 = set()
while stk1:
    curr = stk1.pop()
    if curr in reachable1:
        continue
    reachable1.add(curr)
    stk1.extend(to_d[curr])

stk2 = ['0']
reachable2 = set()
while stk2:
    curr = stk2.pop()
    if curr in reachable2:
        continue
    reachable2.add(curr)
    stk2.extend(from_d[curr])

for x in input_order:
    if x not in reachable1:
        all_ok = False
        print("TRAPPED", x)

for x in input_order:
    if x not in reachable2:
        all_ok = False
        print("UNREACHABLE", x)

if all_ok:
    print("NO PROBLEMS")
    