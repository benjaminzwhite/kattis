# Wood Cutting
# https://open.kattis.com/problems/woodcutting
# TAGS: greedy, sorting
# CP4: 3.4b, Involving Sorting, E
# NOTES:
"""
Reading comprehension: at first I thought you are trying mix customer orders, so you could have
strategies involving e.g cut piece from customer #5 then from #14 then from #3 then #5 again etc. but NO this is not what is asked.

So essentially each customer order, no matter how many pieces of wood they have, should be thought
of as 1 single piece of wood of size = sum(small pieces), and you need to arrange these so that average waiting time is lowest.
So the number of pieces each customer wants is irrelevant, just the sum of their times.

-> sort in ascending order, then accumulate - the accumulator stores how much time person x waits
-> the average waiting time is then THE SUM OF THE ACCUMULATOR i.e. the sum of all the waiting times, divided by number of customers
"""
from itertools import accumulate

T = int(input())

for _ in range(T):
    N = int(input())
    customers = []
    for _ in range(N):
        _, *tmp = map(int, input().split())
        customers.append(sum(tmp))
    
    sum_acc = sum(accumulate(sorted(customers)))
    
    res = sum_acc / N
    
    print(res)

