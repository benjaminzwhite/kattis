# Cooking Water
# https://open.kattis.com/problems/cookingwater
# TAGS: logic
# CP4: 3.2g, Try All Answers
# NOTES:
"""
Found it a quite hard to understand question / reading comprehension: the a, b times are in reference to a CONTINUOUS week/time period.
So it's a kind of "interval" question.
"""
N = int(input())

max_low, min_high = 0, float("inf")
for _ in range(N):
    curr_low, curr_high = map(int, input().split())
    max_low = max(max_low, curr_low)
    min_high = min(min_high, curr_high)

if max_low > min_high:
    print("edward is right")
else:
    print("gunilla has a point")