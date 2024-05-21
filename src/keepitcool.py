# Keep it Cool
# https://open.kattis.com/problems/keepitcool
# TAGS: sorting, greedy
# CP4: 3.4c, Involving Sorting, H
# NOTES:
"""
Left some comments about the logic/conditions being checked locally below
"""
n, m, s, d = map(int, input().split())
fridge = list(map(int, input().split()))

flg = False
# imposs if sum fridge < num students, or new_slots_used == s (since then all slots have warm drink at the front)
if sum(fridge) < m:
    flg = True

xs = sorted((x, i) for i, x in enumerate(fridge))

res = [0] * s
j = 0
while n > 0: # input guarantees can fit all n so no IndexError problems
    to_add = min(n, d - xs[j][0])
    n -= to_add
    res[xs[j][1]] += to_add
    j += 1

# CARE! Need to check an additional condition:
# "are there at least m cold drinks among all the "untouched" fridge slots i.e. those which have NOT had a warm drink placed in front"
if sum(x[0] for x in xs[j:]) < m:
    flg = True

if not flg:
    print(*res)
else:
    print("impossible")