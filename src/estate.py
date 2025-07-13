# Integer Estate Agent
# https://open.kattis.com/problems/estate
# TAGS: mathematics, number theory, array, nice
# CP4: 0, Not In List Yet
# NOTES:
"""
I wrote a detailed solution:

https://github.com/benjaminzwhite/kattis/blob/main/detailed_solutions/estate.md
"""
# -- Precompute the accumulate of 2,3,4,... = 2,5,9,14 --
# CARE! use dummy 0 index value, due to 1-based indexing
N_MAX = 1_000_000
FUNDAMENTALS = [0] # 0 is DUMMY to allow indexing to match k count, see notes
curr = 2
while FUNDAMENTALS[-1] <= N_MAX:
    FUNDAMENTALS.append(FUNDAMENTALS[-1] + curr)
    curr += 1

while (n := int(input())):
    cnt = 0
    k = 1
    while (x := n - FUNDAMENTALS[k]) >= 0:
        cnt += (x % k == 0)
        k += 1

    print(cnt)