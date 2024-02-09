# Above Average
# https://open.kattis.com/problems/aboveaverage
# TAGS: basic, mathematics
# CP4: 3.2h, Math Simulation, Easier
# NOTES:
"""
Optimization/implementation consideration - instead of e.g.:

average = sum(xs) / n
cnt = sum(x > average for x in xs)

you can do:

S = sum(xs)
cnt = sum(n * x > S for x in xs)

which avoids floating point comparisons.
(You perform len(xs) multiplication operations though, instead of 1 division operation.)
"""
C = int(input())

for _ in range(C):
    n, *xs, = map(int, input().split())

    S = sum(xs)
    cnt = sum(n * x > S for x in xs)

    print("{:.3f}%".format(100 * cnt / n))