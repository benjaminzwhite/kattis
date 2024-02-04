# No Thanks!
# https://open.kattis.com/problems/nothanks
# TAGS: array, sorting
# CP4: 2.2e, Sorting, Easier
# NOTES:
"""
Implementation:

I prepend [-1] as dummy element to handle zip behavior : this will handle adding the first element of xs
"""
n = int(input())

xs = [-1] + sorted(map(int, input().split())) # [-1] is dummy element

res = 0
for big, small in zip(xs[1:], xs):
    if big != small + 1:
        res += big

print(res)