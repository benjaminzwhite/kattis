# Planting Trees
# https://open.kattis.com/problems/plantingtrees
# TAGS: sorting, greedy
# CP4: 3.4b, Involving Sorting, E
# NOTES:
"""
Reading comprehension: I was unclear about the +1/-1 day requirement/start vs end of day. 
Just reverse engineered +1/-1 until matched test case
"""
n = int(input())

xs = sorted(map(int, input().split()), reverse=True)

earliest_day = 0

for i, x in enumerate(xs, 1):
    earliest_day = max(earliest_day, i + x + 1) # +1 because of "first full day after" or w/e in description

print(earliest_day)