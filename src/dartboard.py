# Dartboard
# https://open.kattis.com/problems/dartboard
# TAGS: mathematics, calculus
# CP4: 0, Not In List Yet
# NOTES:
"""
You are integrating radially so the infinitesimal is dtheta * r * dr

Integrate over theta which, by angular symmetry, gives the 2*pi term. Then integrate over r:
  _
_/   (1 / pi)  * k * exp(- k * r**2) r * dr

with k = 1 / (2 * sigma**2)

Integral is: (1/pi) * (-1/2) * exp(-k * r**2)

so cancelling factor of 2*pi, and taking definite integral from LOWER_LIMIT to UPPER_LIMIT, we can swap limits and flip - sign:

definite_integral = exp(-k * r**2) [LOWER_r - UPPER_r]
"""
from math import exp

r1, r2, r3, r4, r5, r6 = map(float, input().split())

sigma = float(input())

# CARE! We are using these values as our pairs of "LOWER_r -> UPPER_r" limits of integration, so we
# need 0 for the first interval (from centre, r=0, to the first real circle, r=r1, of bullseye)
radii = [0, r1, r2, r3, r4, r5, r6]

def S(r):
    return exp(- r * r / (2 * sigma * sigma))

integrals = (S(lower_r) - S(upper_r) for lower_r, upper_r in zip(radii, radii[1:]))

coefficients = [50, 25, 210 / 20, 3 * 210 / 20, 210 / 20, 2 * 210 / 20]

res = sum(coeff * integ for coeff, integ in zip(coefficients, integrals))

print(res)