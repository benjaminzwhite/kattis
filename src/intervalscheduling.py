# Interval Scheduling
# https://open.kattis.com/problems/intervalscheduling
# TAGS: greedy, sorting
# CP4: 3.4a, Greedy (Classical)
# NOTES:
"""
Classic exercise of interval scheduling
"""
N = int(input())

xs = []
for _ in range(N):
    l, r = map(int, input().split())
    xs.append((l, r))

xs = sorted(xs, key=lambda x: x[1]) # sort by END TIMES

prev = 0
res = 0
for l, r in xs:
    if l >= prev: # inclusive since consider 1-4, 4-99 not to overlap see description
        prev = r
        res += 1

print(res)