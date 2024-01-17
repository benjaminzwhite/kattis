# The Gourmet
# https://open.kattis.com/problems/gourmeten
# TAGS: dynamic programming
# CP4: 4.6b, Counting Paths, Easier
# NOTES:
"""
- Just standard "how many ways to sum to N given xs" - long winded description.
- For Python, there is a "performance" requirement so recursive approach seems to TLE when I tried
-> So implement dp instead.

---

Implementation after first WA:
Seems sometimes there are input x's that are > target, so if you try initializing the dp[x] with 
them you get index error
-> hence the "if x <= M: dp[x] += 1" if statement in the dp initialization below.
"""
M = int(input())
N = int(input())

xs = []

for _ in range(N):
    xs.append(int(input()))

dp = [0] * (M + 1) # remember, 0 index then you have 1-based indexing for your dp[M] where M is the target we are searching for
for x in xs:
    if x <= M: # seems some inputs can be > M which would cause an index error if you dont have this step
        dp[x] += 1
    
for i in range(M + 1):
    for x in xs:
        if i - x >= 0: # this is also to avoid index error - e.g. if you are at i = 2, dont try x=13 so that you get i-x = -11 index
            dp[i] += dp[i - x]

print(dp[M])