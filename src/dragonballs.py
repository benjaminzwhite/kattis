# Dragon Balls
# https://open.kattis.com/problems/dragonballs
# TAGS: logic, nice, improve
# CP4: 0, Not In List Yet
# NOTES:
"""
TODO: IMPROVE: want to return to see if there is better way to solve/smarter that would reuse the info from multiple queries

---

In my approach below, basically I do a "radar" scan starting from 0,0 each time (this means that the point will always be up and right of you)

(originally was starting at the middle of the board, instead of 0,0, but then have to handle all 4 "quadrants" for given +/- x/y, and it
doesn't result in finding points any faster AFAICT)
"""
XY_MAX = 10**6

n = int(input())
while n:
    print(0, 0)
    d = int(input())
    if d == 0:
        n -= 1
        continue
    
    x = 0
    while (x2 := x * x) <= d:
        y_cand = int((d - x2) ** 0.5)
        if (y_cand <= XY_MAX) and (y_cand * y_cand + x2 == d):
            print(x, y_cand) # if d==25, try e.g 3,4 then...
            dd = int(input())
            if dd == 0:
                break
            print(y_cand, x) # ...try 4,3 to also match d==25
            ddd = int(input())
            if ddd == 0:
                break
        x += 1

    n -= 1