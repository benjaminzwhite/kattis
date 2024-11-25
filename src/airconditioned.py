# Air Conditioned Minions
# https://open.kattis.com/problems/airconditioned
# TAGS: sorting
# CP4: 3.4c, Involving Sorting, H
# NOTES:
"""
It's a sweep-line/intervals type question, draw a test case to get logic:

Consider (1,10) (7,8) (4,5) : if you sort on START you will order as:

[(1,10), (4,5), (7,8)] and since first (s, e) = (1, 10) all subsequent intervals satisfy s_ < e

so you incorrectly will conclude they can all fit in one room.

But if you sort on *END TIME* you get:

[(4,5), (7,8), (1,10)] which correctly shows that in fact 2 rooms are needed
"""
N = int(input())

intervals = []
for _ in range(N):
    s, e = map(int, input().split())
    intervals.append((s, e))

intervals = sorted(intervals, key = lambda t: (t[1], t[0])) # sort by increasing end time
s, e = intervals[0]
rooms = 1

for s_, e_ in intervals[1:]:
    if s_ > e:
        rooms += 1
        s, e = s_, e_

print(rooms)