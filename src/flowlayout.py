# Flow Layout
# https://open.kattis.com/problems/flowlayout
# TAGS: mathematics, geometry
# CP4: 7.2f, Quadrilaterals
# NOTES:
"""
The line w, h = 1000, 1000 is just to trigger processing of last element:

It triggers the "else: ..." statement (since largest actual max_width is 80 < 1000)
so you ensure that last current row is indeed added to total.
"""
while True:
    max_width = int(input())
    if max_width == 0:
        break

    flg = True
    res_W, res_H, curr_W, curr_H = 0, 0, 0, 0
    while flg:
        w, h = map(int, input().split())
        if w == -1 and h == -1:
            w, h = 1000, 1000
            flg = False

        if w + curr_W <= max_width:
            curr_W += w
            curr_H = max(curr_H, h)
        else:
            res_W = max(res_W, curr_W)
            res_H += curr_H
            curr_H, curr_W = h, w

    print(res_W, 'x', res_H)