# Disastrous Downtime
# https://open.kattis.com/problems/downtime
# TAGS: array, queue, nice
# CP4: 2.2a, 1D Array, Medium
# NOTES:
"""
Queue based solution: basically a sweep-line approach to intervals of (x, x + process_time) where here process_time = 1000

CARE! must SORT the inputs ascending for the sweep-line approach (just sort single ints since the 2nd element in the "tuple"
is always +1000 from the first element)

Then: count the largest number of overlapping intervals -> this is the max number of simultaneous tasks / server requests,
then divide this max_simul_tasks result by k, which is the number of tasks per unit time that server can perform AND TAKE CEIL e.g.
if max_simul_tasks is 7 and server can process 2 tasks each then res is CEIL(7/2) = 4, not 3.
(since need 3 full capacity servers + 1 server to handle remaining task)
"""
from collections import deque
from math import ceil

n, k = map(int, input().split())

xs = []

for _ in range(n):
    t = input()
    xs.append(int(t))
    
xs = sorted(xs)

process_time = 1000

q = deque([xs[0] + process_time]) # problem statement ensures input list xs is never empty, n >= 1

max_simul_tasks = 1 # since include first task corresponding to element xs[0]
curr_simul_tasks = 1 # since include first task corresponding to element xs[0]

for x in xs[1:]:
    if x < q[0]:
        curr_simul_tasks += 1
        max_simul_tasks = max(max_simul_tasks, curr_simul_tasks)
    else:
        while q and (x >= q[0]): # update rightmost end-time, until current element x is overlapping with a previous element's end-time (or q is empty -> no overlap whatsover for this element's start position)
            q.popleft()
            curr_simul_tasks -= 1
        curr_simul_tasks += 1
    q.append(x + process_time) # enqueue the current element x's end-time, which is always x + process_time

res = ceil(max_simul_tasks / k)

print(res)