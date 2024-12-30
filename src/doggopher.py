# Dog & Gopher
# https://open.kattis.com/problems/doggopher
# TAGS: mathematics, geometry
# CP4: 8.7e, Geometry+CS
# NOTES:
"""
The easy way to solve is via physical intuition: the dog goes twice speed of the gopher so just imagine that they
are the same speed, but that dog has twice the distance.

The rest is mainly formatting - also I was having fun below with complex numbers: a better implementation for
numerical stability is to compare the squared distances instead.
"""
gx, gy, dx, dy = map(float, input().split())

flg = True

while True:
    try:
        x, y = map(float, input().split())
        if abs(x - dx + (y - dy) * 1j) >= 2 * abs(x - gx + (y - gy) * 1j):
            print(f"The gopher can escape through the hole at ({x:.3f},{y:.3f}).")
            flg = False
            break
    except:
        break

if flg:
    print("The gopher cannot escape.")