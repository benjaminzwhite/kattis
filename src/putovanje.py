# Putovanje
# https://open.kattis.com/problems/putovanje
# TAGS: array, greedy
# CP4: 3.2b, Iterative (Two Loops)
# NOTES:
"""
Reading comprehension/description clarification:
"Also, when Mislav decides to start eating..." means that you can CHOOSE which position you start in the array.

So just try all start positions and then perform greedy accumulation from that start point; take max of all possible.
"""
N, C = map(int, input().split())
xs = list(map(int, input().split()))

best = -1

# try all start positions
for i in range(N):
    cnt = 0
    curr = 0
    for x in xs[i:]:
        if curr + x <= C:
            cnt += 1
            curr += x
    best = max(best, cnt)

print(best)