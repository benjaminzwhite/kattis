# House Lawn
# https://open.kattis.com/problems/houselawn
# TAGS: mathematics, logic
# CP4: 3.2i, Math Simulation, Harder
# NOTES:
"""
Don't know if an iterative/brute force search approach is intended, but here is an analytical solution:

The requirement about being able to mow On Average T lawns, for all positive integer T, is solved by considering
that t / (t + r) is the "effective" amount/proportion of time spent mowing (this formula applies to any time interval).

Implementation:

Can rearrange the various terms to avoid working with floats, good practice.
"""
l, m = map(int, input().split())

min_price = float('inf')
res = []

for _ in range(m):
    n, p, c, t, r = input().split(',')
    p, c, t, r = map(int, (p, c, t, r))
    # "Effective average mowing time proportion" is t/(t+r)
    # So we want:  c * effective_time >= l on average
    # Now rewrite so can avoid convert to floats:
    if c * 10080 * t >= l * (t + r):
        if p < min_price:
            res = [n]
            min_price = p
        elif p == min_price:
            res.append(n)

if res:
    print(*res, sep='\n')
else:
    print("no such mower")