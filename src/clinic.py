# Potion Commotion
# https://open.kattis.com/problems/potioncommotion
# TAGS: priority queue, interpreter
# CP4: 2.3a, Priority Queue
# NOTES:
"""
Reading comprehension/irrelevant inputs - basically just a priority queue:

- the T in parts 1, 2, 3 is NOT THE SAME T!!!! Was confused about description.

- the "priority value" S + K*W is referring to a waiting time W
  but you are given the *arrival times* in the inputs:
  If the absolute value of this quantity were needed you'd have to work backwards from each query to get the exact W
  but if you write S + K*W = S + K*(current_time - arrival_time)
  you see that it's = S + K*current_time - K*arrival_time
  and K*current_time is a CONSTANT FOR ALL PEOPLE IN THE PRIORITY QUEUE since the K is constant for all users so
  you can ignore it for the RELATIVE position of users in the priority queue.
  So long story short, with the given input format, the maxheap invariant is actually S - K*the_time_value_you_are_given
  (then to make things more confusing for Python, we take this with - sign to produce the maxheap behavior with heapq O_o)

- Consequently, in the inputs (since they are sorted in descending order), the exact time at which the doctor makes 
  the type2 queries is IRRELEVANT also (spent a while thinking why they were given in the first place if not needed)
"""
from heapq import heappush, heappop

N, K = map(int, input().split())

maxheap = []
gone = set()

while True:
    try:
        l = input()
        query_type, *xs = l.split()
        if query_type == '1':
            arrival_time, name, severity = xs
            arrival_time = int(arrival_time)
            severity = int(severity)
            val = severity - K * arrival_time # see NOTES above
            heappush(maxheap, (-val, name)) # -val for Python maxheap behavior
        elif query_type == '2':
            while maxheap and maxheap[0][1] in gone:
                gone.discard(maxheap[0][1])
                heappop(maxheap)
            if not maxheap:
                print("doctor takes a break")
            else:
                tmp = heappop(maxheap)
                print(tmp[1])
        elif query_type == '3':
            gone.add(xs[1])
    except EOFError:
        break