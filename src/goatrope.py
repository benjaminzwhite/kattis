# Goat Rope
# https://open.kattis.com/problems/goatrope
# TAGS: basic, mathematics, geometry
# CP4: 7.2b, Lines
# NOTES:
x, y, x1, y1, x2, y2 = map(int, input().split())

if x1 <= x <= x2:
    dx = 0
else:
    dx = min(abs(x - x1), abs(x - x2))

if y1 <= y <= y2:
    dy = 0
else:
    dy = min(abs(y - y1), abs(y - y2))

d = (dx * dx + dy * dy)**0.5

print(d)