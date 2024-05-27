# Pulling Their Weight
# https://open.kattis.com/problems/pullingtheirweight
# TAGS: array, logic
# CP4: 8.7k, Three++ Components, E
# NOTES:
"""
The condition "if acc_weight + (acc_weight + curr_contrib) == total_weight" is checking whether, if we DO ACTUALLY accumulate the
current contribution to the accumulated weight (i.e. "on the left") will we obtain:

"left weight" i.e. acc_weight == total_weight - acc_weight - curr_contribution <- this is the more logical way to view it

Note that this handles cases when curr_contribution is 0 nicely since we try ALL POSSIBLE w from 1,2...MAX_W

So in the testcase with 1,2,3,6 we have:

  w  = 1,2,3,4,5,6
acc  = 1,3,6,6,6,10
curr = 1,2,3,0,0,6
total is 12

So we see that at w = 4, acc_weight = 6, total=12, curr_contrib=0, so 6 == 12-6-0 **OK**

But for w = 3, acc_weight = 6, total=12, curr_contrib = 3 so 6 != 12-6-3 **NOT OK**
(i.e. we need for this value of w=3 to be included on the left for balancing, but w=4 NO we do not)
"""
MAX_W = 20_000

n = int(input())

total_weight = 0
cnt = [0] * (MAX_W + 10) # +10 is sentinel
for _ in range(n):
    x = int(input())
    total_weight += x
    cnt[x] += 1

acc_weight = 0
for w in range(1, MAX_W + 1):
    curr_contrib = w * cnt[w] # NOTE: see above, since we try ALL weight values w, even those that DO NOT APPEAR in input, this allows triggering of result when we reach the "w+1" value that divides range. e.g. with the 1,2,3,6 value this triggers the w=4 result
    if acc_weight + (acc_weight + curr_contrib) == total_weight: #  (i.e. acc_weight == total_weight - acc_weight - curr_contribution ) <--- this is the more logical way to view it; think of it with the test case 3,8,10,11 when you are at the w=10 value; YOU ARE DOING THIS CHECK STEP *BEFORE* adding the 1*10 = 10 weight to the left_acc_weight value
        print(w)
        break
    else:
        acc_weight += curr_contrib