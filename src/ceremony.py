# Opening Ceremony
# https://open.kattis.com/problems/ceremony
# TAGS: sorting, greedy, logic
# CP4: 3.4c, Involving Sorting, H
# NOTES:
"""
CARE! The best result is always <= n (since worst case: you can always destroy n buildings individually)

So must initialize the best variable to n (not to 1e9 or float('inf') or whatever).
"""
n = int(input())

xs = sorted(map(int, input().split()))

best = n # n is always an option!!! e.g. if you init best = 1e9, code below will fail for eg. xs = [10,20,30] <- best is 3 here not 10+1+1=12

# used i in range(n) instead of enumerate(xs) as its clearer to see that we are looking at i'th element xs[i] at each step.
for i in range(n):
    #                  v---------------- destroy this building and all buildings smaller than it in xs[i] horizontal shots
    best = min(best, xs[i] + (n - i - 1))
    #                          ^-------- destroy remaining (n - i - 1) buildings in 1x vertical shot each

print(best)