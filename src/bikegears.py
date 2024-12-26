# Bike Gears
# https://open.kattis.com/problems/bikegears
# TAGS: sorting
# CP4: 3.2b, Iterative (Two Loops)
# NOTES:
"""
Straightforward, but you get wrong answer WA if you do simple lambda sort with float x[0]/x[1] value,
so I used cmp_to_key to compare integers only i.e. not f1/b1 vs f2/b2 but rather f1*b2 vs f2*b1 etc.
"""
from functools import cmp_to_key

def gear_cmp(gear1, gear2):
	"""
	Custom compare function for complex sorting requirement
	"""
    f1, b1 = gear1
    f2, b2 = gear2

    #f1/b1 < f2/b2
    if f1 * b2 <= f2 * b1:
        if f1 < f2:
            return -2
        else:
            return -1
    else:
        return 0

F, B = map(int, input().split())
fs = list(map(int, input().split()))
bs = list(map(int, input().split()))

gears = []

for f in fs:
    for b in bs:
        gears.append((f, b))

res = sorted(gears, key=cmp_to_key(gear_cmp))

for x, y in res:
    print(f"({x},{y})")