# Crazy Driver
# https://open.kattis.com/problems/driver
# TAGS: greedy, logic
# CP4: 3.4e, Non Classical, Easier
# NOTES:
"""
Greedy approach works - think of it with words / time travel: "What I should have done before reaching this gate etc.":
If you know you are going to be early at any given gate, then you should loiter doing back-and-forth between the
2 cheapest PREVIOUS gates, for the smallest amount of time such that you would arrive at the given gate when it is open.

Ex:
opentime=  2   4   7    100
cost=       99  *3*  45

Here if you get to gate with opentime=100 early, you "should have" spent the excess wait time moving between the gates
whose transit cost is 3 such that you arrive at time=100 or time=101 (since you can always arrive within 1 minute
of opening due to 2 way streets and taking 1 min per unit trip)
"""
from math import ceil

N = int(input())

costs = list(map(int, input().split()))
times = list(map(int, input().split()))
times = times[1:]

min_gate = float("inf")
curr_time = 0
total_cost = 0
for c, t in zip(costs, times):
    curr_time += 1
    min_gate = min(min_gate, c)
    if t > curr_time: # if we're early, we'll just waste our time at the cheapest available 1+1=2unit journey between 2 PREVIOUS gates before this one
        time_adjustment = 2 * ceil((t - curr_time) / 2)
        curr_time += time_adjustment
        total_cost += time_adjustment * min_gate
    total_cost += c

print(total_cost)