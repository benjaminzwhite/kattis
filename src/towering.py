# A Towering Problem
# https://open.kattis.com/problems/towering
# TAGS: brute force
# CP4: 3.2e, Iterative (Permutation)
# NOTES:
from itertools import permutations

inps = list(map(int, input().split()))

xs = inps[:6]
tower1, tower2 = inps[6:]

# can do with next(), just clearer like this:
for a, b, c, x, y, z in permutations(xs):
	if (a > b > c) and (x > y > z) and (a + b + c == tower1) and (x + y + z == tower2):
		print(a,b,c,x,y,z)
		break