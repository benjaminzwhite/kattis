# Rectangle Area
# https://open.kattis.com/problems/rectanglearea
# TAGS: basic
# CP4: 7.2f, Quadrilaterals
# NOTES:
a, b, p, q = map(float, input().split())

print(abs((a - p) * (b - q)))