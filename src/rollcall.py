# Roll Call
# https://open.kattis.com/problems/rollcall
# TAGS: sorting
# CP4: 2.3e, Hash Table (map), E
# NOTES:
import sys
from collections import Counter

xs = []
c = Counter()

for line in sys.stdin:
	fst, snd = line.split()
	c.update([fst])
	xs.append((fst, snd))

xs = sorted(xs, key=lambda t:(t[1], t[0]))

for x in xs:
	if c[x[0]] == 1:
		print(x[0])
	else:
		print(x[0], x[1])