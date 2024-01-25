# Ragged Right
# https://open.kattis.com/problems/raggedright
# TAGS: basic
# CP4: 6.2f, Really Ad Hoc
# NOTES:
"""
Reading comprehension - the max length line is relative to ALL lines,
but then the formula to use is applied to all EXCEPT LAST line
"""
import sys

ls = []
max_len = 0

for line in sys.stdin:
	curr_len = len(line) # TODO: check if line.strip() needed ?
	ls.append(curr_len)
	max_len = max(max_len, curr_len)

res = sum((max_len - curr_len)**2 for curr_len in ls[:-1])

print(res)