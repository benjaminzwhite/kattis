# Birds on a Wire
# https://open.kattis.com/problems/birds
# TAGS: sorting
# CP4: 3.4c, Involving Sorting, H
# NOTES:
"""
Basically you have 2 poles with an exclusion zone of 6 cm either side.
Start left window at +6, and then for the terminating condition you can model the right pole as a bird,
but you place it NOT at len-6, but rather at len-6+d. Here the +d is so that its effective exclusion zone is: len-6+d - d = len-6
(since birds are modelled with d exclusion zone)
"""
l, d, n = map(int, input().split())

birds = [l - 6 + d] # model the right-most pole as the last bird
for _ in range(n):
    birds.append(int(input()))

birds = sorted(birds)
curr_left = 6
res = 0

for right in birds:
    interval = right - d - curr_left
    can_sit = interval // d + 1
    res += can_sit
    curr_left = right + d
    
print(res)