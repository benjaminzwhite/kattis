# Identifying Map Tiles
# https://open.kattis.com/problems/maptiles2
# TAGS: grid, nice, improve
# CP4: 5.2g, Grid
# NOTES:
"""
Nice little puzzle - way underrated at 1.6 difficulty compared to other green exercises O_o

---

Couldn't find a quick formula approach at the moment TODO: IMPROVE

---

Since you expand 2 * each x and y direction each time, I work backwards from the size (which is a power of 2)
doing a kind of binary search of LEFT/RIGHT x and LEFT/RIGHT y each step
"""
s = input()

xl, xr = 1, 2**len(s) # NOTE: I use e,g 1,2,3...7,8 instead of indices. Need to -1 at the end since it wants 0 based indexing
yl, yr = 1, 2**len(s)

for c in s:
    xm = (xl + xr) // 2
    ym = (yl + yr) // 2

    if c == '0': # x,y are in "left" of the current range of numbers
        xr = xm
        yr = ym
    elif c == '2': # x is in left, y is in right of current range of numbers
        xr = xm
        yl = ym
    elif c == '1': # x is in right, y is in left of current range of numbers
        xl = xm
        yr = ym
    elif c == '3': # x,y are in "right" of current range of numbers
        xl = xm
        yl = ym

print(len(s), xr - 1, yr - 1) # 0 based indexing