# Stamp Combinations
# https://open.kattis.com/problems/stampcombinations
# TAGS: array, improve
# CP4: 0, Not In List Yet
# NOTES:
"""
TODO: IMPROVE: I think I can speed up quite a bit, but this approach works.

---

In this approach you compute forward and backwards accumlate of the values.
This will work since it at worse will perform "num_queries * full_search_of_n_elements " operations, using the usual Two-Sum problem type approach:
then just do the  usual "Leetcode Two-Sum" approach of looking up the "complement/needed value" to reach the target:

--> use fwd_acc (WLOG) as the LOOKUP set()
--> use back_acc (WLOG) as the iterating list, in ascending order:
==> for a given query/target: e.g. "20" -> iterate over back_acc: [1,4,5,8,11,15,28,1001,...] and for each back_acc value, check if the
    complement = Query - Back_acc_value is in the fwd_acc() LOOKUP set.
    if so, this defines a forward range (from the left) and a backwards range (ie from the right) that together sum to the target and
    which are "cuttable at each end" so that you are left with a single piece of paper [this is the requirement of the problem]

Implementation Notes:

CARE! You need to initially add {0} / [0] to the fwd_acc set and back_acc list before any accumulated values because this corresponds to 
cases where your range is entirely on one side or the other.
(Otherwise current solution will fail for a testcase like "can you make 0 with xs = 1 2 3" -> the answer is YES, just don't cut any stamps)

Also intially I forgot to implement a check that the "ranges" are NON OVERLAPPING -> for example, my initial solution would say, for 
xs = 5 5 5 5
that you CAN produce e.g. 35 because e.g. 20 appears in fwd_acc and 15 appears in back_acc

--> SO redesigned a bit: fwd_acc is now a dict which stores as KEYS the fwd_acc values and as VALUES the *POSITION* at which this acc occurs
--> when you iterate over back_acc now, with enumerating it with 'j', then the i in fwd_acc and the j in back_acc are counting the total
number of blocks used from the left and right interval respecitively (i=0,1,2....num_blocks, and j=0,1,2...num_blocks)
==> so the lookup condition is extended now to include a 2nd check:
    If query - back_acc in fwd_acc{} *AND* if i+j <= num_blocks, then it's a nonoverlapping range
"""
from itertools import accumulate

num_blocks, num_queries = map(int, input().split())
xs = list(map(int, input().split()))

fa = 0
fwd_acc = {}
for i, x in enumerate([0] + xs): #careful, need to add 0 as 0 is a valid option
    fa += x
    fwd_acc[fa] = i

back_acc = [0] + list(accumulate(xs[::-1])) # careful, need to add 0 as 0 is a valid option

# queries
for _ in range(num_queries):
    q = int(input())
    res = "No"
    for j, b in enumerate(back_acc):
        if b > q:
            break
        if q - b in fwd_acc and fwd_acc[q - b] + j <= num_blocks: # see notes, need to check "physical" number of blocks otherwise e.g. target = 35, xs=5 5 5 5 would return YES when it is impossible ofcourse
            res = "Yes"
            break
    print(res)