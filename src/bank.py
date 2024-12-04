# Bank Queue
# https://open.kattis.com/problems/bank
# TAGS: priority queue, greedy
# CP4: 3.4e, Non Classical, Easier
# NOTES:
"""
Nice exercise: basically, consider e.g. edge case of wait-time t=0 user with cash = 10, but wait-time t=4 having 4 users with cash = 1_000_000; then you 
want to be able to skip the user at t=0 and stagger the ones who are willing to wait up to t=4,and use them at 0,1,2,3 with their huge cash

-> So you work from righe to left i.e. decreasing order of time. Forget about implementation for now, just consider:

At t=9, the only values that will ever be worth considering are the 9 highest cash amounts [nb - off by 1 here I think due to 0 indexing, doesn't matter for the argument]
since, in any case,the 10,11,... highest will never be worth taking (due to limited number of timeslots from 0 -> 9)

By a similar argument, the 8 highest cash amounts contributed by t=8 people are worth considering BUT ONLY IN RELATION TO THE VALUES FROM 9 PREVIOUSLY
e.g. if from 9 you have [100,99,98,50,50,40,40,20,10] and
e.g. if from 8 you have [45,45,11,11,5,5,5,5]

Then you should "update" the list from 9 to include all the elements that are higher than the lowest on an index by index basis:
here you take 45,45 and discard 20,10 from 9

While building a solution like this, sorting and removing each step, I realised it's just a MAXHEAP (lol).
You don't need to track exact numbers; just add ALL THE VALUES FROM TIME T_max TO MAXHEAP, THEN += RES BY THE CURRENT MAX ELEMENT,
THEN -=1 the current time (moving R->L from T_max to t=0), add the new available cash amounts, and again pop the maxheap etc.
You can do this since at each time t=9, t=8 etc YOU KNOW THAT IN PRINCIPLE ANY OF THE VALUES ON THE HEAP CAN BE
USED AT *ANY TIME* EARLIER THAN CURRENT t (think about it)
"""
from heapq import heappush, heappop

N, T = map(int, input().split())

cash_at_time = [[] for _ in range(T)] # for each possible max-wait time we add all the cash values that are available at that time to this array

for _ in range(N):
    cash, t = map(int, input().split())
    cash_at_time[t].append(cash)
    
maxheap = []
res = 0

for t in range(T - 1, -1, -1):
    for cash in cash_at_time[t]:
        heappush(maxheap, -cash) # -cash due to Python maxheap behavior
    if maxheap: # IMPORTANT, else get error when e.g. you skip times e.g. imagine T=10 and cash_at_time = [ [2],[2,4,5],[54,22],[],[],[],[],[],[],[1000]] or whatever - as you move R->L the heap will be empty for a while until you encounter i=2,i=1,i=0 lists to add to the maxheap
        res += abs(heappop(maxheap)) # abs since the cash values are negative, due to Python MAXheap behavior

print(res)