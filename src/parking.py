# Parking
# https://open.kattis.com/problems/parking
# TAGS: basic
# CP4: 1.6e, Real Life, Easier
# NOTES:
prices = list(map(int, input().split()))

xs = []

for _ in range(3):
    o, c = map(int, input().split())
    xs.append((o, 0))
    xs.append((c, 1))

xs = sorted(xs)

curr_drivers = 0
prev_x = xs[0][0]
res = 0

for x, open_close in xs:
    res += curr_drivers * prices[curr_drivers-1] * (x - prev_x)
    if open_close == 0:
        curr_drivers += 1
    else:
        curr_drivers -= 1
    prev_x = x

print(res)