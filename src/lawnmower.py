# Lawn Mower
# https://open.kattis.com/problems/lawnmower
# TAGS: array, sorting
# CP4: 2.2f, Sorting, Harder
# NOTES:
"""
Interval covering kind of exercise.
"""
while True:
    nx, ny, w = map(float, input().split())
    if nx == 0 and ny == 0:
        break

    d = w / 2
    xs = list(map(float, input().split()))
    ys = list(map(float, input().split()))

    x_intervals = [(x - d, x + d) for x in sorted(xs)]
    y_intervals = [(y - d, y + d) for y in sorted(ys)]

    flg = True
    xr = 0
    for l, r in x_intervals:
        if l > xr:
            flg = False
            break
        else:
            xr = max(xr, r)

    yr = 0
    for l, r in y_intervals:
        if l > yr:
            flg = False
            break
        else:
            yr = max(yr, r)

    if flg and xr >= 75 and yr >= 100:
        print("YES")
    else:
        print("NO")