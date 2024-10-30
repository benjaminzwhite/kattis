# Square Deal
# https://open.kattis.com/problems/squaredeal
# TAGS: sorting, logic
# CP4: 3.2f, Iterative (Combination)
# NOTES:
"""
You can brute force with combinations, but you can use a bit of logic before to make it clearer:

Easier if you think first and realise that each rectangle has a BIG and SMALL dimension - then the various configs become easier to enumerate:

case 1: there are 3 blocks stacked on top of eachother -> they must have the same BIG dimension
(otherwise if they had same SMALL dimension, the sum of the 3 BIGS would > 1 SMALL -> impossible to make a square)

case 2-multiple: there are 2 blocks stacked on top of a 3rd -> the third MUST BE THE ONE WITH THE BIGGEST BIG DIMENSION
-> so, sort blocks by their big dimension; I call "y3, x3" below the BIG/SMALL sides of the biggest block

Now there are 4 possible ways to arrange the 2 remaining:
basically whether they are joined on their "x1 x2" side, "x1 y2" side, "y1 x2" side or "y1 y2" side (do a drawing it's easier)

In all these 4 cases, the condition is that: 

1) shared sides have equal size
2) when you add 1) to the size of x3, you get y3 (to make a square)
3) that the sum of the "other 2" dimenions == y3
"""
xs = []

for _ in range(3):
    big, small = map(int, input().split())
    if small > big:
    	big, small = small, big
    xs.append((big, small))

# here sort in reverse order, so that xs[0] contains the "biggest big-dimension"
# (confusing, it's basically a leftover from my original approach - could just have sorted(xs)[2] to be BIGGEST and sorted(xs)[0] to be smallest -.-)
xs = sorted(xs, reverse=True)

y3, x3 = xs[0] # CARE! I have (y,x) in my xs list since I take y to be the BIG dimension
y2, x2 = xs[1]
y1, x1 = xs[2]

def is_good(xa, xb, ya, yb):
    return (ya + yb == y3) and (xa == xb) and (xa + x3 == y3)

# these are the 4 possible pairings of the 2-blocks in the configuration where you have largest block as base and 2 others fitting together on top of it.
PAIRINGS = [(x1, x2, y1, y2), (x1, y2, y1, x2), (y1, x2, x1, y2), (y1, y2, x1, x2)]

# in the "or": condition 1 is when all 3 blocks have same BIG dimension, condition 2 is trying the 4 possible pairing configurations
if (y3 == y2 == y1 and (x3 + x2 + x1) == y3) or any(is_good(*pairing) for pairing in PAIRINGS):
    print("YES")
else:
    print("NO")