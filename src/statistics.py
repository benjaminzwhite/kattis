# Statistics
# https://open.kattis.com/problems/statistics
# TAGS: basic
# CP4: 1.4e, Control Flow
# NOTES:
import sys

for case, line in enumerate(sys.stdin, 1):
	_, *xs = map(int, line.split())

	mn, mx = min(xs), max(xs)

	print(f"Case {case}: {mn} {mx} {mx - mn}")