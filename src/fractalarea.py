# Fractal Area
# https://open.kattis.com/problems/fractalarea
# TAGS: mathematics, geometry
# CP4: 7.2c, Circles
# NOTES:
from math import pi

T = int(input())

for _ in range(T):
    r, n = map(int, input().split())

    num_circles = [1, 4]
    for _ in range(n - 2):
        num_circles.append(num_circles[-1] * 3)

    total_area = 0
 
    for i, c in enumerate(num_circles):
        if i < n:
            total_area += c * r * r * 0.5**(2 * i)

    print(pi * total_area)