# Cookie Selection
# https://open.kattis.com/problems/cookieselection
# TAGS: heap, mathematics
# CP4: 2.3i, Order Statistics Tree
# NOTES:
"""
For the code part, I'm just reusing my logic from my solution of Continuous Median - had to rewrite the basic fact that
here the question wants the "right" heap to always be the larger of the 2, so that for Odd number of elements in total,
the RIGHT heap has n//2+1 elements while left will have n//2. 

Then you rebalance accordingly - if n was ODD, then no need to rebalace after popping from right
if n was EVEN eg. had [1,3,4] [10, 20, 25] and popped 10 on this iteration, then check if len(left) > len(right)
(by +1 element always) and then pop the max element of LEFT to RIGHT to rebalance

---

For input handling, I got annoying WA a few times (was not used to Kattis/OJ inputs, so might be my mistake):
I spent ages until I modified to check x[0] != '#' rather than x != '#' - I HAVE NO IDEA WHY??? 
Because if s = '#' then print(s == '#', s[0] == '#') gives True True, so i have no idea what is going on with input format?
Maybe some trailing whitespace in the file format, or I don't understand sys.stdin properly?

"""
import sys
from heapq import heappush, heappop

left, right = [], []

for x in sys.stdin:
    if x[0] != '#':
        x = int(x)
        heappush(left, -x)
        largest_left = heappop(left)
        heappush(right, -largest_left)

        if len(right) > len(left) + 1:
            smallest_right = heappop(right)
            heappush(left, -smallest_right)

    else:
        median = right[0]
        print(median)
        heappop(right)

        if len(right) < len(left):
            heappush(right, -heappop(left))