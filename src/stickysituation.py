# Sticky Situation
# https://open.kattis.com/problems/stickysituation
# TAGS: mathematics, geometry, logic
# CP4: 7.2e, Triangles + Circles
# NOTES:
N = int(input())

xs = sorted(map(int, input().split()))

flg = False
for i in range(N - 3 + 1):
    a, b, c = xs[i:i + 3]
    if a + b > c:
        flg = True
        break

if flg:
    print("possible")
else:
    print("impossible")