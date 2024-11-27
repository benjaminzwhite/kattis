# Distributing Ballot Boxes
# https://open.kattis.com/problems/ballotboxes
# TAGS: binary search
# CP4: 3.4d, Involving PQ
# NOTES:
"""
CARE! THE MAX N is 500_000 but the max POPULATION is 5_000_000 NOT 500_000 (when you read the parameters it's easy to confuse the 2)

---

Binary search; guess a "final" value for the max people per box across all the villages; if it is possible to assign/divide
each village's population according to this max value, then certainly it is possible for all smaller numbers so keep increasing
the guess accordingly, or decrease if not etc.

e.g. N = 2, B = 7 ,  village 1 = 200 people, village 2= 500 people
Suppose we say in the end the MAX number of people per ballot box, in the optimal assignment, is 10 people_per_box
-> is this possible/consistent with each village? We check:
1/ it would imply that village 1 has at least 200/10 = 20 ballot boxes
2/ it would imply that village 2 has at least 500/10 = 50 ballot boxes
We find that 20+50 = 70 ballot boxes, but this is > B=7 (the ACTUAL number we have)
So this guess, 10 people per box, is inconsistent with B=7, so we must guess MORE PEOPLE PER BOX. etc.
"""
from math import ceil

while True:
    N, B = map(int, input().split())
    if (N, B) == (-1, -1):
        break
    
    populations = []
    for _ in range(N):
        p = int(input())
        populations.append(p)
        
    l, r = 1, 5_000_000
    while l <= r:
        max_people_per_box = (l + r) // 2
        curr_boxes_required = 0
        ok = True
        
        for p in populations:
            curr_boxes_required += ceil(p / max_people_per_box)
            if curr_boxes_required > B:
                l = max_people_per_box + 1
                ok = False
                break
        if ok:
            r = max_people_per_box - 1
    
    print(l)
    input()