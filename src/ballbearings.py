# Ball Bearings
# https://open.kattis.com/problems/ballbearings
# TAGS: mathematics, geometry
# CP4: 7.2c, Circles
# NOTES:
"""
Hard to do the drawing in ASCII art O_o for my Notes but basically:

-draw a big circle of diameter D and draw 2 adjacent small circles inside the big one, as in exercise illustration, each of diameter d separated by s
-Draw the isoceles triangle from the centre of big circle to the 2 centres of the small circles, call this distance r
-The opening angle of this wedge, call it 2*alpha, is bisected by the perpendicular from the centre that passes through the midpoint of the line that 
 joins the 2 centres of the small circles

Now the geometry is clear: you are trying to create as many such wedges as possible.

-> The line joining the centre of the 2 small circles has length - assuming closest packing - of 1/2*d + s + 1/2d = s+d
-> Then we can solve for alpha (half the opening angle 2*alpha from the centre of big circle to the centres of the 2 small circles)
-> r * sin alpha = 1/2 distance from centres of 2 small circles (draw it to see the right triangle geometry)
-> r * sin alpha = 1/2 ( s + d ) [see above]
Also r is just radius_of_big_circle - radius_of_small_circle = D/2 - d/2 = 1/2 (D-d)

So solving we get:

-> sin alpha = 1/2 (s+d) / r = 1/2 (s+d) / 1/2 (D-d) = (s+d)/(D-d)   

So we want to fit as many wedges of angle 2*alpha (! nb, we have calculated the half angle so far) in the circle, so:

-> res = 2 pi / (2*alpha) = pi / alpha [and take the floor of the result]
"""
from math import pi, asin, floor

T = int(input())
for _ in range(T):
    D, d, s = map(float, input().split())

    alpha = asin((d + s) / (D - d))

    res = floor(pi / alpha) # 2*pi total angle / 2*alpha <-- angle occupied by each wedge

    print(res)