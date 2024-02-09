# Head Guard
# https://open.kattis.com/problems/headguard
# TAGS: array
# CP4: 1.6m, Input Parsing (Iter)
# NOTES:
"""
Can implement run length encoding with itertools groupby
"""
import sys
from itertools import groupby

for line in sys.stdin:
	s = line.rstrip() # not sure if you actually need to rstrip each line for spaces

	res = ''.join(str(len([*g])) + k for k, g in groupby(s))

	print(res)