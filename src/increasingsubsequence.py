# Increasing Subsequence
# https://open.kattis.com/problems/increasingsubsequence
# TAGS: dynamic programming, improve
# CP4: 3.5b, LIS
# NOTES:
"""
TODO: IMPROVE:

There is some extra condition about lexicographical order - basically you want e.g. [2,4,5] instead of [3,4,5]
So I consider all candidates at each step and only add the lexicographically smaller at each step
My implementation isn't great: I'm trying to find MINIMUM lexicographic while in a mixed key:
(I'm taking the "minimum" of the negative ength, then 2nd key is sort on X)
"""
while True:
    n, *xs, = map(int, input().split())
    if n == 0:
        break
    dp = [[] for _ in range(len(xs))]
    for i, x in enumerate(xs):
        curr = [x]
        candidates = []
        for prev in dp:
            if prev and prev[-1] < x and len(prev) + 1 > len(curr):
                candidates.append(prev + [x])
        if candidates:
            dp[i] = min(candidates, key=lambda e: (-len(e), e))
        else:
            dp[i] = curr
    res = min(dp, key=lambda e: (-len(e), e))
    print(len(res), *res)