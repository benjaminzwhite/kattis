# Working From Home
# https://open.kattis.com/problems/workingfromhome
# TAGS: logic
# CP4: 1.6f, Real Life, Medium
# NOTES:
"""
This is a straightforward exercise but is ranked 4.5+, maybe because the working variables
are a bit confusing. My first approach was updating the variable 'm' directly, but that is
NOT the interpretation that is correct.

Here is my reading comprehension summary:

- there is a CONSTANT/FIXED TARGET which he calls m
- but you are only supposed to UPDATE a separate 2nd "CURR_TARGET" which is NOT the same as m
"""
from math import ceil

m, p, n = map(int, input().split())

res = 0
curr_target = m # curr_target is INITIALLY equal to the "fixed target" m

for _ in range(n):
	w = int(input())

	if w >= curr_target:
		res += 1

	curr_target = ceil(m - (w - curr_target) * (p / 100)) # update curr_target, BUT NOT m 

print(res)