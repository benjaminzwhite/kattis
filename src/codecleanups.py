# Code Cleanups
# https://open.kattis.com/problems/codecleanups
# TAGS: array
# CP4: 1.4j, Medium
# NOTES:
n = int(input())
xs = list(map(int, input().split()))
reset_idx = 0
cnt = 0

for i,x in enumerate(xs):
    dirty_interval = xs[reset_idx:i]
    left_uncleaned = sum(x - y for y in dirty_interval) # this is what the dirtyness would be today at index i if we did not clean prior to today
    if left_uncleaned >= 20: # it it is >= 20 then we should have cleaned, and reset so that today we are not dirty
        reset_idx = i
        cnt += 1

print(cnt+1)