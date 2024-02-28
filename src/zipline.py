# Zipline
# https://open.kattis.com/problems/zipline
# TAGS: mathematics, calculus, geometry, physics
# CP4: 3.3c, Ternary Search & Others
# NOTES:
"""
You don't need to ternary search, you can also solve analytically with a bit of geometry:

Express L1 and L2 as sqrt(g**2 + x**2) and sqrt(h**2 + (w-x)**2)

L = L1 + L2, set dL/dx=0 
-> [...] -> x / sqrt(g**2 + x**2) = (w-x) / sqrt(h**2 + (w-x)**2)
-> [...] -> x**2 h**2 = g**2 (w-x)**2 <--- here this just means multiplication i.e. x**2 times h**2 etc.

Solving quadratic with:

a = (g**2 - h**2)
b = -g**2 *2*w
c = g**2w**2

gives the x1 (physically meaningful) value of x, put it back into L1 and L2 to get total L.

---

NOTE: g == h case is degenerate, the above ^^^ leads to a == 0 in quadratic formula, it's the symmetric case 

-> so solve by finding either of the L1 or L2 - they are the same - and then L = 2*L1 = 2*L2

---

NOTE: the question is asking about maintaining a height r above the ground at all times;
this is just equivalent to reducing input heights g and h to effective heights:
g' = g - r and 
h' = h - r (see code below)
"""
from math import sqrt

n = int(input())

for _ in range(n):
    w, g, h, r = map(int, input().split())

    g -= r # if we must be always r above ground then effective g' and h' are g - r and h - r
    h -= r

    if g == h:
        L = sqrt(g * g + (w / 2)**2)
        max_cable_len = L + L
    else:
        a = (g**2 - h**2)
        b = -(g**2) * 2 * w
        c = (g**2) * (w**2)

        x1 = (-b - sqrt(b * b - 4 * a * c)) / (2 * a) # -root sign is the physically meaningful one

        L1 = sqrt(g * g + x1 * x1)
        L2 = sqrt(h * h + (w - x1)**2)

        max_cable_len = L1 + L2

    min_cable_len = sqrt((h - g)**2 + w**2) # the hypothenuse between the height of h and the height of g, with horiz distance w

    print(min_cable_len, max_cable_len)