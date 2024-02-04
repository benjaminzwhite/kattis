# Unlock Pattern
# https://open.kattis.com/problems/unlockpattern
# TAGS: mathematics, geometry
# CP4: 7.4a, 3D Geometry
# NOTES:
"""
See comments for formula.

Can simplify algebraically to avoid lots of floating point calcs.
"""
from math import pi

while True:
    D, V = map(int, input().split())
    if (D, V) == (0, 0):
        break

    """
    big_cone = 1/3 * pi * (D/2) ** 3
    small_cone = 1/3 * pi * (d/2) ** 3
    big_cyl = 1/4 * pi * D ** 3
    small_cyl = 1/4 * pi * d ** 3
    empty_vol = big_cyl - small_cyl - 2*(big_cone - small_cone)

    Simplifying: V = (D**3 - d**3)(pi/4 - pi/12) = (D**3 - d**3)*(pi/6)
    """

    tmp = D * D * D - 6 * V / pi

    res = pow(tmp, 1 / 3)

    print(res)