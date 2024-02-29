# Annoyed Coworkers
# https://open.kattis.com/problems/annoyedcoworkers
# TAGS: priority queue, greedy, nice
# CP4: 3.4d, Involving PQ
# NOTES:
"""
Nice exercise, a few subtle points and an elegant reformulation helps solve.

---

The clearest way to understand is to design a testcase that looks something like the one included at the bottom of these Notes.

Imagine it's with 2 requests and 4 colleagues.

Basically as you can see; if you heappop based on initial a value only, you may create immediately a huge a+d value. 
It's actually better to "leave that colleague alone". In my example, colleague 1 seems OK but then will return to the minheap with a value 1+100 = 101.

Whereas an optimal solution is - counterintuitively(?!) - to ask the colleague with the huge upfront a-value twice, because
after 2 requests he is only at 57 which is optimal solution compared to the 3 other colleagues.

So the key insight/elegant way to solve is: you should heappush actually "how angry they WOULD BE AFTER NEXT ASK"

You can do this by heappushing into the original minheap (a + d) instead of a.

When you heappop these values, they represent the anger level AFTER the given help_request -> so can take a max(most_annoyed, curr) as you heappop.

---

Custom testcase mentioned in text above, 4 colleagues:

1 100 <----- you really dont want to ask this guy for help, not even once, even though he starts out as not angry at all
2 85
3 91
55 1 <---- you actually want to repeatedly ask this guy for help, even though he is initially the angriest
"""
from heapq import heappush, heappop

help_requests, colleagues = map(int, input().split())

most_annoyed = 0
minheap = []
for _ in range(colleagues):
    a, d = map(int, input().split())
    most_annoyed = max(most_annoyed, a) # update - I think you need to do this to handle cases where there is an input where a value is already greater than anything updated during all the heappop stuff; e.g. a worked with 100000 100000 who never gets used
    heappush(minheap, (a + d, d))

for _ in range(help_requests):
    curr, d_ = heappop(minheap) # see discussion - now by initializing minheap with a+d, we are viewing the decisions NOT as "current lowest anger" but rather "what will create the smallest max anger AFTER this request"
    most_annoyed = max(most_annoyed, curr)
    heappush(minheap, (curr + d_, d_))

print(most_annoyed)