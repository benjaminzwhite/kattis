# Songbook
# https://open.kattis.com/problems/sangbok
# TAGS: sorting, greedy
# CP4: 3.4b, Involving Sorting, E
# NOTES:
"""
CARE! Need to convert time, t, to seconds as input is in minutes and xs are in seconds for some reason
"""
t, n = map(int, input().split())
xs = sorted(map(int, input().split()))

# should just do t = t * 60 once here
acc = 0
i = 0
while i < len(xs):
    if acc + xs[i] <= t * 60:
        acc += xs[i]
    else:
        break
    i += 1

print(acc)