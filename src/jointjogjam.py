# Joint Jog Jam
# https://open.kattis.com/problems/jointjogjam
# TAGS: geometry, logic
# CP4: 7.2a, Points
# NOTES:
"""
They either get closer or further apart (monotonically) so the distance between them is always either:

- decreasing (so distance at beginnining is maximal separation)
- or increasing (so distance at end is maximal separation)
"""
a, b, c, d, e, f, g, h = map(int, input().split())

res = max((a - c)**2 + (b - d)**2, (e - g)**2 + (f - h)**2)

print(res ** 0.5)