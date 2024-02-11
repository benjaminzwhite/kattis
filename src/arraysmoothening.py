# Array Smoothening
# https://open.kattis.com/problems/arraysmoothening
# TAGS: priority queue, greedy, improve
# CP4: 3.4d, Involving PQ
# NOTES:
"""
TODO: IMPROVE

I have a feeling there may be a non PQ approach that is much simpler, but didn't see it immediately.

---

Unrelated to exercise specifically, but had WA due to a subtle bug that I had not thought about/seen before:

Originally I was trying to be clever and initializing my maxheap as:
maxheap = [-v for v in c.values()]

and I was expecting to just heappop from it later. In my AC code below, this ends up being replaced by correct code:
maxheap = []
for v in c.values():
    heappush(maxheap, -v)

=> The reason the first code DOESN'T work is because when you first enter the subsequent loop
(i.e. the loop that begins for _ in range(can_remove): ...) the maxheap is NOT A HEAP YET !!!!

It is still just a list, and so its first element is NOT THE ROOT NODE but is just the first of
the v's added during the above comprehension.
"""
from collections import Counter
from heapq import heappush, heappop

_, can_remove = map(int, input().split())
xs = map(int, input().split())

c = Counter(xs)

# See Notes above about subtle bug I found at this step
maxheap = []
for v in c.values():
    heappush(maxheap, -v) # the first heappush call makes maxheap into an actual heap! Remember also -v to get maxheap behavior in Python

for _ in range(can_remove):
    curr_max_cnt = heappop(maxheap)
    heappush(maxheap, curr_max_cnt + 1) # curr_max_cnt is < 0 due to Python maxheap so "decrement" it by adding +1 O_o

if maxheap:
    res = -heappop(maxheap)
else:
    res = 0

print(res)