# Track Smoothing
# https://open.kattis.com/problems/tracksmoothing
# TAGS: geometry, logic
# CP4: 7.2c, Circles
# NOTES:
"""
Just draw a clear diagram - decompose the corners/vertices into their circular components.
"""
from math import pi

t = int(input())

for _ in range(t):
    r, n = map(int, input().split())
    first_x, first_y = map(int, input().split())
    prev_x, prev_y = first_x, first_y
    
    length = 0
    for _ in range(n - 1):
        x, y = map(int, input().split())
        length += ((x - prev_x)**2 + (y - prev_y)**2)**0.5
        prev_x, prev_y = x, y
    length += ((first_x - prev_x)**2 + (first_y - prev_y)**2)**0.5

    circumference = 2 * pi * r
    if circumference > length:
        print("Not possible")
    else:
        print((length - circumference) / length)