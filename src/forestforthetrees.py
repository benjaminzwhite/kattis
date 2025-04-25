# Forest for the Trees
# https://open.kattis.com/problems/forestforthetrees
# TAGS: mathematics, number theory
# CP4: 8.7a, BSTA+Other, Easier
# NOTES:
"""
You can solve this with binary search, but here is an analytical solution.

I left comments locally below.
"""
from math import gcd

xb, yb = map(int, input().split())
x1, y1, x2, y2 = map(int, input().split())

g = gcd(xb, yb)

# the first point on the line of sight between 0,0 and xb,yb is 1 "increment" of the "gcd vector"
# e.g. in testcase; target is (2,6) which has trees at every "vector" (+1,+3)
first_point = (xb // g, yb // g)

# the penultimate point on the line of sight is "N-1" increments of the gcd vector; i.e. it is the location that 
# is just 1 more vector incremement AWAY FROM the final point xb, yb
last_point = (xb - xb // g, yb - yb // g)

# Two possibilities for line of sight OK:
# 1) if the first point/tree we encounter on the line IS THE TARGET ITSELF
#    (e.g. if target is (1,1) for example or more interestingly, if xb,yb relatively prime so gcd=1 -> then no tree will block, regardless of clearing)
# 2) else: the first_point and last_points define a "visibility rectangle" that needs to be completely cleared if you are to see the target
#    so check if indeed all the x coords and y coords within the rectangle defined by the first_point and last_points [NOTE THIS IS NOT
#    THE SAME RECTANGLE AS THE "cleared" ONE FROM INPUT - WE ARE EFFECTIVELY CHECKING IF THE FORMER IS CONTAINED IN THE LATTER] 
#    are cleared, then you have line of sight:
first_x, first_y = first_point
last_x, last_y = last_point
if (first_point == (xb, yb)) or ((x1 <= first_x <= last_x <= x2) and (y1 <= first_y <= last_y <= y2)):
    print("Yes")
else:
    print("No")
    # the first point that blocks is either immediately the first one on the "line" to target 
    # OR, if the cleared area covers it, the first point "after" the rectangle
    immediate_x, immediate_y = first_x, first_y # it's the same variable, I'm just changing names for clarity

    if immediate_x < x1 or immediate_y < y1: # CARE! tricky logic: I had 'and' RATHER THAN 'or' HERE, ON FIRST SUBMIT AND GOT WA
    	# (You need 'or' as this covers the case where the first tree is outside and "before" the clearing rectangle.)
        # The "clearing" occurs after the very first tree, so it is the very first tree that will block us in this case
        print(immediate_x, immediate_y)
    else:
        # the "clearing" occurs immediately where we are standing, so we are looking for first tree outside
        # of the clearing, that is on the line to the target
        # -> to handle geometry of the clearing, think in terms of multiples of the "gcd vector"
        # -> keep adding +1 gcd vector, until you get out of the clearing: the smallest multiple depends on the x/y geometry of the rectangle
        last_multiple_within_rectangle = min(x2 // immediate_x, y2 // immediate_y)
        first_multiple_outside_rectangle = last_multiple_within_rectangle + 1
        far_x = first_x * first_multiple_outside_rectangle
        far_y = first_y * first_multiple_outside_rectangle
        print(far_x, far_y) 