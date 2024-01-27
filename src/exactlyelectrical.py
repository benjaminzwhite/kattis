# Exactly Electrical
# https://open.kattis.com/problems/exactlyelectrical
# TAGS: logic, geometry
# CP4: 1.4i, Still Easy
# NOTES:
"""
CARE! There are actually 2 conditions to check, not just the t >= distance one.

As long as any "excess battery" you have is even, you can use up the excess battery
by repeatedly moving +/-1 (for a total of 2 units of distance each round trip) from your final location
"""
a, b = map(int, input().split())
c, d = map(int, input().split())

t = int(input())

distance = abs(a - c) + abs(b - d)

if t >= distance and (t - distance) % 2 == 0:
    print("Y")
else:
    print("N")