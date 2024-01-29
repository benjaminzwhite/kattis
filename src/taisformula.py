# Tai's formula
# https://open.kattis.com/problems/taisformula
# TAGS: basic, geometry
# CP4: 7.2f, Quadrilaterals
# NOTES:
N = int(input())
xs = []

for _ in range(N):
    t, v = map(float, input().split())
    xs.append((t, v))

res = sum((t2 - t1) * (v2 + v1) / 2 for (t1, v1), (t2, v2) in zip(xs, xs[1:]))

print(res / 1000)