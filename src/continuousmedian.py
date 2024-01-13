# Continuous Median
# https://open.kattis.com/problems/continuousmedian
# TAGS: heap, nice
# CP4: 2.3i, Order Statistics Tree
# NOTES:
"""
Really nice exercise.

I left comments in code directly - we are creating a "left" and "right" heap in order to track
the values that are closest to the median value.

Rest is some tricky implementation, checking lengths of the left and right heaps.

Also, CARE! due to Python heapq library: you implement a max-heap using the library's min-heap,
but with NEGATIVE values.
"""
from heapq import heappush, heappop

T = int(input())

for _ in range(T):
    N = int(input())
    
    xs = map(int, input().split())
    
    left, right = [], []
    sum_medians = 0
    
    for x in xs:
        # e.g. for input 1 3 6 2 7 8 after five steps, our heaps look like:
        #
        # left: -3, -2, -1 <= Python min-heap representation of ACTUAL max-heap => 1, 2, 3 <- 3 is the max element
        # right: 6,7
        #
        # representation of: 1,2,3|6,7 is therefore
        #                 -3,-2,-1|6,7
        # --------------------------------------------
        # we push to left and send max of left to right
        heappush(left, -x)
        largest_left = heappop(left)
        heappush(right, -largest_left)
        
        # we balance so that left has the excess +1 element on its side
        if len(right) > len(left):
            smallest_right = heappop(right)
            heappush(left, -smallest_right)
    
        if len(left) != len(right):
            # imbalanced left and right halves; we use left half to store excess +1 element so the median is found as the largest
            # element in left (n.b. that it due to Python implementation as min heap it is the MOST NEGATIVE VALUE)
            median = -left[0] # see above, Python implementation of the max heap is as min heap with NEGATIVE VALUES
            sum_medians += median
        else:
            # balanced left and right halves: the largest element in left and smallest element in right contribute to the median
            largest_left = -left[0]
            smallest_right = right[0]
            median = (largest_left + smallest_right) / 2
            # NOTE THAT IN THIS SPECIFIC PROBLEM, we round DOWN this median to have an integer value (problem statement)
            # HENCE THE int() BELOW:
            sum_medians += int(median)
    
    print(sum_medians)