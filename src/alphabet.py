# Alphabet
# https://open.kattis.com/problems/alphabet
# TAGS: longest increasing subsequence
# CP4: 3.5c, LIS
# NOTES:
"""
This is the O(n**2) Longest Increasing Subsequence LIS approach with dynamic programming, since input is small here.
"""
xs = input()

dp = [1] * len(xs)

for i in range(len(xs)):
    for j in range(i):
        if ord(xs[i]) > ord(xs[j]):
            dp[i] = max(dp[i], dp[j] + 1)

res = 26 - max(dp)

print(res)