# Jigsaw
# https://open.kattis.com/problems/jigsaw
# TAGS: mathematics, brute force
# CP4: 0, Not In List Yet
# NOTES:
"""
Below approach is the brute force approach I used while debugging my first WA.

The reason was that the case m == 0 is allowed: I'm not quite sure what this is supposed to correspond to O_o
(So I added the m > 0 check for the main loop)

---

If you want to code golf/be smarter, then you can just solve the simultaneous eqns: need to make sure
that the discriminant (e**2 - 16*m) you obtain initially is positive though.
"""
c, e, m = map(int, input().split())

d = 1
flg = True
# UPDATE: added m > 0 check after first WA O_o
if m > 0:
    flg = False
    while d * d <= m:
        if m % d == 0:
            if 2 * (d + (m // d)) == e:
                #print(d,m//d," is consistent with edge squares: ",e)
                #print("this corresponds to a",(d+2), " x ", (m//d)+2, " puzzle")
                flg = True
                res = sorted([d + 2, (m // d) + 2], reverse=True)
                break
        d += 1
else:
    if e % 2 != 0: # not needed due to above?
        flg = False
    else:
        res = [2, 2 + e // 2]

if c != 4:
    flg = False

if flg: 
    print(*res)
else:
    print("impossible")