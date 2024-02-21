# The Rectangles Are Surrounding Us!
# https://open.kattis.com/problems/rectanglesurrounding
# TAGS: mathematics, geometry, combinatorics
# CP4: 7.2f, Quadrilaterals
# NOTES:
"""
Note that a,b is bottom left point and c,d is top right point and you are counting the SQUARES inside, not the integer points.
-> so the number of squares corresponds to taking c, and d, upper limits as EXCLUSIVE.

e.g. for (1,1) to (2,2) there are 4 integer points on the boundary but it's the 1 full square inside that is being counted.

Therefore: there are as many squares in the area as there are BOTTOM LEFT INTEGER POINTS. So by summing range(a,c) and
range(b,d) you are "peeling off" the top row and rightmost col's integer points (draw a diagram if you want to visualize)
"""
while True:
    n = int(input())
    if n == 0:
        break

    N_MAX = 500 # coordinates are 0 -> 500 *INCLUSIVE*
    arr = [[0] * (N_MAX + 1) for _ in range(N_MAX + 1)]
    res = 0

    for _ in range(n):
        a, b, c, d = map(int, input().split())
        for row in range(a, c):
            for col in range(b, d):
                if arr[row][col] == 0:
                    res += 1
                arr[row][col] = 1

    print(res)