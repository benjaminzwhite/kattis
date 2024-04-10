# Mumble Rap
# https://open.kattis.com/problems/mumblerap
# TAGS: string
# CP4: 1.6m, Input Parsing (Iter)
# NOTES:
"""
Many ways to solve, used groupby for fun O_o
"""
from itertools import groupby

N = int(input())

s = input()

res = -float('inf')

for k, g in groupby(s, lambda x: x.isdigit()):
	if k:
		curr = int(''.join(list(g)))
		res = max(res, curr)

print(res)