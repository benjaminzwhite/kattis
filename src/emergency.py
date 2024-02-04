# Emergency Contest Running
# https://open.kattis.com/problems/emergency
# TAGS: logic, graph, nice
# CP4: 8.7h, Mathematics+Other
# NOTES:
"""
Nice algorithmic/reasoning exercise:

Draw the graph for e.g. k=3 or k=2 cases and convince yourself/prove that optimal strategy
is to travel between lowest multiple of k to highest multiple of k, then make up the difference using 
the +1 moves from m to m+1 as many times as needed.

---

CARE! Must take min(res, n - 1) since n - 1 is always an option (applies when k >= n since then it's correct
to just shuffle from m to m + 1 all the way round circle)
"""
n, k = map(int, input().split())

# first integer > 0 that is divisible by k:
first = k

# the largest integer <= n - 1 that is divisble by k:
last = k * ((n - 1) // k)

# res:
# a) walk to first in: k steps
# b) walk from first to last in: 1 step
# c) walk from last to (n - 1) in: (n - 1) - last steps
res = k + 1 + (n - 1) - last

res = min(res, n - 1) # see comment in notes about why n - 1 is possible also.

print(res)