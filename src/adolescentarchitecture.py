# Adolescent Architecture
# https://open.kattis.com/problems/adolescentarchitecture
# TAGS: sorting
# CP4: 0, Not In List Yet
# NOTES:
"""
Sort the shapes in increasing area since in all cases will need the shapes to be in nondecreasing area
-> the tricky thing then is that even if area above < area below, if the SHAPES/FAMILY MISMATCH then they still might overlap
e.g. a circle might have smaller area but overhang the square below it or vice versa (?)
-> so pairwise through sorted Blocks, if the type below==type above, no need to check (since they are sorted already you know the
block above must be <= area of below, hence since they are same shape, must have radius/linear size <= of the one below)
-> However if the 2 shapes mismatch, work out the geometry and determine if the above one does indeed fit entirely within footprint of the below one

---

Implementation notes:

I got a WA at first: it was because the author gives as inputs the RADIUS OF EACH CIRCLE, but the FULL LENGTH of each SQUARE
(not very logical to me, either do diameter + fullside length, or radius + halflength O_o oh well) 
so I was off by a factor of 2* in my first submission.

CARE! also, I append a dummy element after sorting, to trigger processing of last real Block.
"""
from collections import namedtuple
from math import pi, sqrt

Block = namedtuple("block", ["area", "family", "radius"]) # I used "family" instead of "type" to avoid keyword clash

n = int(input())
xs = []
for _ in range(n):
    fam, r = input().split()
    r = int(r)
    if fam == "cube":
        a = r * r
    else:
        a = pi * r * r
    tmp = Block(a, fam, r)
    xs.append(tmp)

xs = sorted(xs, key=lambda x: -x.area) # SORT ALL BLOCKS/SHAPES BY AREA, REGARDLESS OF THEIR TYPE: then do the type mismatch later once they are sorted
xs.append(Block(-1, 'cube', -1)) # DUMMY LAST ELEMENT

flg = True
res = []
for below, above in zip(xs, xs[1:]):
    if below.family == "cube" and above.family == "cylinder":
        # 2*radius of cylinder needs to be <= side length of square
        if 2 * above.radius > below.radius: # CARE! weird input format the cube "radius" is its FULL LENGTH; problem statement mixes CIRCLE RADIUS and CUBE FULL LENGTH -.-
            flg = False
            break
    if below.family == "cylinder" and above.family == "cube":
        # diag of square needs to <= 2*radius cylinder
        if 2 * (above.radius)**2 > 4 * (below.radius)**2: # do without sqrt(2), just take squares so use ints only
            flg = False
            break

    res.append((below.family, below.radius))

if flg:
    for fam, r in res[::-1]:
        print(fam, r)
else:
    print("impossible")