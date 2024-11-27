# Assigning Workstations
# https://open.kattis.com/problems/workstations
# TAGS: priority queue
# CP4: 3.4d, Involving PQ
# NOTES:
"""
Description is quite unclear to me; it's not obvious WHAT SPECIFICALLY IS BEING ASKED TO RETURN even after rereading multiple times.

Originally I thought it meant: you have "5" users, so in principle should unlock "5" PCs, but what is max_number_of_pcs needed
at any given time; and take e.g "5" minus that answer, to get the "number of unlocked PCs saved"

But in reality it wants you to measure:
HOW MANY EVENTS OCCUR IN YOUR QUEUE IN WHICH A USER ARRIVES WITHIN A m TIME UNIT INTERVAL OF ANOTHER USER LEAVING


Also got a RTE - it seems there are cases when priority queue becomes empty, so you have to manually add "if PQ and ..."
(in case you check pq[0] and pq doesn't exist). Question says "You may assume that there are always enough workstations available" so
I assumed such a situation could not happen.
"""
from heapq import heappop, heappush

n, m = map(int, input().split())

xs = []
for _ in range(n):
    l, r = map(int, input().split())
    xs.append((l, r))

xs = sorted(xs)

unlockings_avoided = 0
pq = []
heappush(pq, xs[0][0] + xs[0][1]) # PQ OF EARLIEST TIMES STATION(S) ARE AVAILABLE

for x in xs[1:]:
    # if opening time is before the earliest possible time, then need to create a new workstation
    if pq and (x[0] < pq[0]):
        heappush(pq, x[0] + x[1])
    elif pq and (pq[0] <= x[0] <= pq[0] + m):
        # can avoid unlocking
        unlockings_avoided += 1
        heappop(pq)
        heappush(pq, x[0] + x[1])
    else:
        # can't avoid unlocking
        while pq and (pq[0] + m < x[0]):
            heappop(pq)
        if pq and (pq[0] <= x[0] <= pq[0] + m): #NOTE IMPORTANT: tried removing this and got W.A.; once you have removed the stations in above 2 lines, need to check the front of the PQ one last time if it NOW can be assigned to the current arrival user, now that the user is within the shutoff time
            unlockings_avoided += 1
            heappop(pq)
        heappush(pq, x[0] + x[1])

print(unlockings_avoided)