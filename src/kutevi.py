# Kutevi
# https://open.kattis.com/problems/kutevi
# TAGS: dynamic programming
# CP4: 3.5g, DP level 2
# NOTES:
"""
dp[r][c] states: here the rows will track number of operations we have performed, columns are the angles we have reached.

Initially row 0 -> place True in all the columns corresponding to INPUT ANGLES e.g. 10, 20, 45 if they are the inputs.

Then, propagate down to next row: for each angle X in row r that is reachable, we can reach X+{a}; X-{a}; X  where {a} is ALL THE ANGLES IN THE INPUT 

So update row r+1 -> set the corresponding columns X+a, X-a, X to True.
CARE! Note the 3, not 2, options: remember to propagate X itself!!! If you can reach it in r rows, can ofc reach it in r+1 rows!

Final dp row dp[-1] after 360 steps contains all the values that can be reached as True.
"""
N, K = map(int, input().split())
angles = list(map(int, input().split()))
queries = list(map(int, input().split())) # don't think you need list, only iterate once

dp = [[False] * 360 for _ in range(360 + 1)] # do up to 360 operations; worst case (I think?) is if one of the angles is prime; need to += p 360 times to generate all possible values from that start angle

for x in angles:
    dp[0][x] = True

for r in range(360):
    for this_angle, can_reach in enumerate(dp[r]):
        if can_reach:
            for angle in angles:
                dp[r + 1][(this_angle + angle) % 360] = True
                dp[r + 1][this_angle] = True # CARE! remember to propagate dp state to r+1 for this_angle also!!
                dp[r + 1][(this_angle - angle) % 360] = True

for q in queries:
    if dp[-1][q]:
        print("YES")
    else:
        print("NO")