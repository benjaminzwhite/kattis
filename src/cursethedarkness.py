# Curse the Darkness
# https://open.kattis.com/problems/cursethedarkness
# TAGS: basic, geometry
# CP4: 7.2a, Points
# NOTES:
"""
Radius of candle illumination is always 8 units:
Compare radius squared, 64, to avoid taking square roots of squared distance.
"""
m = int(input())

for _ in range(m):
    X, Y = map(float, input().split())
    n = int(input())
    F = 0
    for _ in range(n):
        x, y = map(float, input().split())
        if (X - x)**2 + (Y - y)**2 <= 64:
            F = 1
    if F == 0:
        print("curse the darkness")
    else:
        print("light a candle")