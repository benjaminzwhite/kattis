# Implementation Irregularities
# https://open.kattis.com/problems/implementationirregularities
# TAGS: greedy, sorting
# CP4: 3.4c, Involving Sorting, H
# NOTES:
"""
A bit of reading comprehension (maybe it's easier if you understand rules/settings of ICPC contests ?):

Basically you have a total actual amount of time needed to solve tasks, and an "arrival time" at which they were solved.

Therefore if e.g. total time needed = 37 took place at t = 4, then clearly that wasn't done by 1 computer because you needed
at least ceil(37/4) = 10 computers working in parallel for the current accumulated task load of 37 time units to be finished by t=4.

Once you understand the problem statement then the solution is clearly a greedy one:

Just think of "how much accumulated real time is required to perform all the tasks up until NOW" where NOW is updated for
each t you are given in the input
"""
from math import ceil

n = int(input())

needed = map(int, input().split())
times = map(int, input().split())

ts = [(time, need) for time, need in zip(times, needed)]

ts = sorted(ts)

computers = 1
acc_time = 0

# should rewrite to just be
# for (time, need) in sorted(ts): ...
# instead of using t[0] and t[1] O_o
for t in ts:
    if t[0] == -1:
        continue
    acc_time += t[1]
    computers = max(computers, ceil(acc_time / t[0]))

print(computers)