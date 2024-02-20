# Code Cleanups
# https://open.kattis.com/problems/codecleanups
# TAGS: array, nice
# CP4: 1.4j, Medium
# NOTES:
"""
Nice exercise.

Basically start approach was, for each day d = 1,2,...365, check if the days in xs that are prior to that day can all be left untidyied or not.
In other words, for each d, compute the dirtyness of the dirty interval < d.
But insight is: instead of doing it for all d, you can just use the x values themselves in the given xs:

for each x you encounter, check whether the entire currently left_uncleaned interval has a dirtyness < 20.

IF YES, then you are ok and dont need to clean on this x either
IF NO, then *there must have been a clean that took place between today and the end of the last added x in the left_uncleaned interval*
in otherwords, there must have been a point where that left_uncleaned inteval had dirtyness >= 20.
IT DOESNT MATTER WHEN, just that it happened, so you += cleans by 1 regardless and reset the left_uncleaned interval TO START TODAY (i.e. at the current index)

So basically you have a sliding window with left idx originally 0, and move LEFT_IDX  to current_idx, i, whenever the interval has dirtyness >= 20
"""
n = int(input())
xs = list(map(int, input().split()))

reset_idx = 0
cnt = 0

for i, x in enumerate(xs):
    dirty_interval = xs[reset_idx:i]
    left_uncleaned = sum(x - y for y in dirty_interval) # this is what the dirtyness would be today at index i if we did not clean prior to today
    if left_uncleaned >= 20: # it it is >= 20 then we should have cleaned, and reset so that today we are not dirty
        reset_idx = i
        cnt += 1

print(cnt + 1)