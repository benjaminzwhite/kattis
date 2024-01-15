# Piece of Cake!
# https://open.kattis.com/problems/pieceofcake2
# TAGS: basic, geometry
# CP4: 7.2f, Quadrilaterals
# NOTES:
"""
- Note it is maximum of the 4 possible regions formed.
- Also the HEIGHT IS ALWAYS = 4, to form the volume 4* ... etc.
- You can also simplify the formula below significantly if you want to code golf
"""
n, h, v = map(int, input().split())

q = h * v

print(4 * max(n * (n - v - h) + q, q, v * n - q, h * n - q))