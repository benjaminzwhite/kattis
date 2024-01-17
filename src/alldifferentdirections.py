# All Different Directions
# https://open.kattis.com/problems/alldifferentdirections
# TAGS: geometry
# CP4: 7.2d, Triangles (Trig)
# NOTES:
"""
Relatively easy; just input parsing and reading comprehension - basically repeated add vectors.
"""
from math import cos, sin, pi, sqrt

while True:
    n = int(input())
    if n == 0:
        break

    finals = []

    for _ in range(n):
        x, y, _, alpha, *rest = input().split()
        x = float(x)
        y = float(y)
        alpha = float(alpha)
        
        i = 0
        while i < len(rest):
            op, val = rest[i], rest[i+1]
            if op == "turn":
                alpha += float(val)
            elif op == "walk":
                val = float(val)
                x += val * cos(2 * pi * alpha / 360) # should use math.radians() really
                y += val * sin(2 * pi * alpha / 360) # should use math.radians() really
            i += 2
        finals.append((x, y))

    average_x = sum(t[0] for t in finals) / n
    average_y = sum(t[1] for t in finals) / n
    worst_direction = max(sqrt((t[0] - average_x)**2 + (t[1] - average_y)**2) for t in finals)

    print(average_x, average_y, worst_direction)