# WordSpin
# https://open.kattis.com/problems/wordspin
# TAGS: string, nice
# CP4: 0, Not In List Yet
# NOTES:
"""
I wrote a detailed solution:

https://github.com/benjaminzwhite/kattis/blob/main/detailed_solutions/wordspin.md
"""
s, target = input().split()

res = 0

prev = 0
for c_s, c_target in zip(map(ord, s), map(ord, target)):
    delta = c_target - c_s

    # check if in same direction as previous move:
    # if NOT in same direction, cannot use previous move to piggyback:
    if not prev or (delta < 0 and prev > 0) or (delta > 0 and prev < 0):
        res += abs(delta)
    elif abs(delta) > abs(prev):
        res += abs(delta) - abs(prev)

    prev = delta

print(res)