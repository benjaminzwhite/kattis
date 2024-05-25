# Maximum Fix
# https://open.kattis.com/problems/maximumfix
# TAGS: array
# CP4: 0, Not In List Yet
# NOTES:
"""
Go through input xs, for each x store the size of the shift needed to send that x to the "correct" index.
For each shift value, incremement a counter of how many x values need that shift value.
Then, among all possible shift values, find the one which leads to the most x values being sent to correct index.

CARE! you need to handle negative values since the shift must always be positive.

Also, need to handle tie break condition - return the result with the lowest k (see comment in code below)

---

Implementation note:

n_max is 10**6 so the cnt array approach isn't too bad, but can solve using a dict{} instead, which potentially will lead
to fewer than 10**6 keys being stored, and also when iterating (for j,y in cnt_dict.items()...)
"""
n = int(input())
xs = list(map(int, input().split()))

cnt = [0] * (n + 1)
for i, x in enumerate(xs, 1):
    shift_needed = i - x
    if shift_needed < 0:
        shift_needed += n
    cnt[shift_needed] += 1

k, f = 0, 0
for j, y in enumerate(cnt):
    if y > f: # do strictly > so that in case of tie break we keep the result with lowest k (as required by exercise)
        k, f = j, y

print(k, f)