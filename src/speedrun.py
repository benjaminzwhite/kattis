# Speedrun
# https://open.kattis.com/problems/speedrun
# TAGS: array, sorting, greedy
# CP4: 3.4a, Greedy (Classical)
# NOTES:
"""
Interval problem - count maximum number of non overlapping intervals
"""
G, N = map(int, input().split())

intervals = []

for _ in range(N):
    s, e = map(int, input().split())
    intervals.append((s, e))

intervals = sorted(intervals, key=lambda t: (t[1], t[0]))

max_poss = 1
s, e = intervals[0]

for s_, e_ in intervals[1:]:
    if s_ >= e:
        max_poss += 1
        s, e = s_, e_

if max_poss >= G:
    print("YES")
else:
    print("NO")