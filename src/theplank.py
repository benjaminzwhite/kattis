# The Plank
# https://open.kattis.com/problems/theplank
# TAGS: basic, recurrence
# CP4: 3.2a, Pre-calculate-able
# NOTES:
"""
- I didn't see that input has n <= 24, so solving the recurrence to get a performant iterative solution is not in fact needed.

- So here is a recursive solution that also solves the problem in Python for n = 24:

from functools import lru_cache

@lru_cache
def rec_plank(n):
	if n == 0:
		return 1
	if n == 1:
		return 1
	if n == 2:
		return 2
	else:
		return rec_plank(n-3) + rec_plank(n-2) + rec_plank(n-1)

n = int(input())

print(rec_plank(n)) # n=24 gives answer 1389537 in agreement with iterative approach below.

"""
n = int(input())

a,b,c = 1,1,2

for _ in range(n):
    a,b,c = b,c,a+b+c
    
print(a)