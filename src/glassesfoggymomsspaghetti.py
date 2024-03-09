# Glasses Foggy, Mom's Spaghetti
# https://open.kattis.com/problems/glassesfoggymomsspaghetti
# TAGS: mathematics, geometry
# CP4: 7.2d, Triangles (Trig)
# NOTES:
"""
Probably a much simpler way to solve the trigonometry, but below was useful while debugging.

---

The "tricky" part is that apparently it is allowed to have the lower -h/2 part go BELOW THE y=0 axis
(the illustration shows above) so with the below interpretation you have to be careful with the sign of the angles
and whether or not you add or substract them.

I'm using u,v,w as the angles formed by the 3 lines in the "fan" RELATIVE TO THE HORIZONTAL y=0 that's
why it's tricky because when they are all 3 above you can get the relative angles between the 3 lines
easily, but when 3rd line is below y=0 axis you get the sign stuff O_o
i.e. not always v-w, sometimes its v+w for the relative angle
"""
from math import sqrt, acos, cos, sin

d, x, y, h = map(int, input().split())

# angles u,v,w are the "fan" angles to the horizontal as you come in from top: outer boundary, centreline, lower boundary
u = acos(x / sqrt(x**2 + (y + (h / 2))**2))
v = acos(x / sqrt(x**2 + y**2))
w = acos(x / sqrt(x**2 + (y - (h / 2))**2))

theta1 = u - v
res1 = d * sin(theta1) / cos(theta1)

# Consider when h is very large and y very small e.g. case d,x,y,h = map(int, "1 5 1 10".split()) 
# in such cases you can see the 3rd line of the fan is below the y=0 line (y=-4 with the above ^ example)
# so v-w is NOT the correct angle between centreline and lower boundary in such cases - you need to take v+w instead
if h / 2 <= y: # CASE WHERE GEOMETRY INVOLVES ALL THE 3 LINES OF THE FAN ABOVE THE y=0 LINE
    theta2 = v - w
else: # CASE WHERE THE GEOMETRY HAS LOWER BOUNDARY (LINE #3) BELOW THE y=0 LINE
    theta2 = v + w
res2 = d * sin(theta2) / cos(theta2)

print(abs(res1) + abs(res2))