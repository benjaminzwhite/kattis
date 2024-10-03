# Knigs of the Forest
# https://open.kattis.com/problems/knigsoftheforest
# TAGS: priority queue
# CP4: 2.3a, Priority Queue
# NOTES:
"""
Reading comprehension - the question is a bit unclear; use of the word "pool" is bad imho:

The exercise says "The pool of contenders stays constant over the years"
It should say "THE MINIMUM SIZE/NUMBER OF CONTENDERS, k, FOR A TOURNAMENT TO BE VALID STAYS CONSTANT OVER THE YEARS" something like that.

So it's just a queue question, heappop the highest element each "year" EXCEPT YOU STOP WHEN DOING SO WOULD TAKE YOUR QUEUE SIZE < k.

So: Maintain counter starting at Year = 2011.
Each year, heappop and see if the strength == target_strength (the strenght of the Karl you want to win)
If it is, then (since all strenghts are distinct), this must be the year your moose won.
If not, year += 1, add the (unique) moose from year += 1 and repeat
(To track the mooses in order of years of arrival I use a 2nd heap, minheap, with their years and strengths)
"""
from heapq import heappush, heappop

k, n = map(int, input().split())
karl_yr, karl_str = map(int, input().split())

all_moose = [(karl_yr, karl_str)]

for _ in range(n + k - 2):
    y, s = map(int, input().split())
    heappush(all_moose, (y, s))

curr_tournament = []
curr_yr = 2011

for _ in range(k):
    y, s = heappop(all_moose)
    heappush(curr_tournament, -s) # max heap to get winner

flg = True

while len(curr_tournament) == k: # this requirement should be explained much more clearly in description imho
    # get winner as pop
    winner_str = abs(heappop(curr_tournament))
    if winner_str == karl_str:
        print(curr_yr)
        flg = False
        break
    elif all_moose: # need this condition since at last element chronologically my implemention will try to replenish the k-1 moose with new moose, when in fact we have run out
        y, s = heappop(all_moose)
        heappush(curr_tournament, -s)
        curr_yr += 1

if flg:
    print("unknown")