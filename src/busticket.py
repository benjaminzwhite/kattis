# Bus Ticket
# https://open.kattis.com/problems/busticket
# TAGS: dynamic programming
# CP4: 8.3a, DP level 3
# NOTES:
"""
Notes/comments in code below directly.
"""
MAX_N = 10 ** 6 + 5

dp = [0] * MAX_N

s, p, m, n = map(int, input().split())

xs = sorted(map(int, input().split()))

# the earliest possible trip on which we can buy a p-ticket is the first; it will "cover us" up until the "+m"th day
# where +m -/+ 1 due to the wording being incomprehensible -> will try with +m-1 since that works for testcase but try all combinations/interpretations if get WA
curr_period_start_idx = 0
end_curr_period = xs[0] + m - 1 # it's so confusing whether the m is inclusive or not due to how it's badly explained "number of days until you make trip"!?!?

for i in range(n):
    option1 = dp[i - 1] + s # buy the singletrip ticket, cost s
    option2 = float('inf')
    if xs[i] <= end_curr_period:
        # we are still within the current period of a p ticket, so look at dp cost to get there and add cost p to get here
        if curr_period_start_idx == 0:
            # we are still within current_period of the first trip, so in principle we could *STILL* cover all the trips
            # so far up to here with a single p ticket
            option2 = p
        else:
            # if curr_period_start_idx > 0, we have had to solve a subproblem i.e. there are earlier trips "outside/to the left"
            # of our lookbehind range at this current index -> therefore, we look at the best result at that location 
            # as stored in the dp and then take the single p ticket from that point to here
            option2 = dp[curr_period_start_idx] + p
    else:
        # we are NOT within current_period of a p ticket, so we move the period_start_idx to the first possible
        # location that does indeed cover us at this current index i with a p ticket -> we can then take option2 from that start_idx 
        # so: move curr_period_start_idx until we are within its range:
        while (xs[curr_period_start_idx] + m - 1) < xs[i]:
            curr_period_start_idx += 1
        
        # last move overshoots so undo:
        curr_period_start_idx -= 1
        option2 = dp[curr_period_start_idx] + p

    dp[i] = min(option1, option2)

res = dp[n - 1] # the smallest possible cost to make the trips up to and including the nth

print(res)