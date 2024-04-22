# Distance
# https://open.kattis.com/problems/distance
# TAGS: mathematics, geometry, array, nice
# CP4: 8.7h, Mathematics+Other
# NOTES:
"""
This is a really nice exercise - I wrote a detailed solution:

https://github.com/benjaminzwhite/kattis/blob/main/detailed_solutions/distance.md
"""
from collections import Counter

def clever_sum_manhattan(arr):
    c = Counter(arr)
    xs = sorted(c.keys()) # CARE! IMPORTANT TO TAKE SET OF x VALUES/use keys() so you only count once the distinct possible x values

    res = 0
    num_points_to_the_right = len(arr) # CARE! This however is no longer the distinct x values, but rather the ACTUAL NUMBER OF POINTS
    acc_points_to_move_now = 0
    for xl, xr in zip(xs, xs[1:]):
        hm_points_at_xl = c[xl]
        acc_points_to_move_now += hm_points_at_xl
        num_points_to_the_right -= hm_points_at_xl
        next_distance_to_move = abs(xl - xr)
        # need to perform this move, with all current acc points, how many times? ans: as many times as there are points to the right
        res += acc_points_to_move_now * next_distance_to_move * num_points_to_the_right

    return res

N = int(input())

x_values = []
y_values = []
for _ in range(N):
    x, y = map(int, input().split())
    x_values.append(x)
    y_values.append(y)

res = clever_sum_manhattan(x_values) + clever_sum_manhattan(y_values)

print(res)