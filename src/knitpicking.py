# Knitpicking
# https://open.kattis.com/problems/knitpicking
# TAGS: logic, nice
# CP4: 3.4f, Non-Classical, Easier
# NOTES:
"""
Just consider for each sock type what the worse case is: pick all the LEFT socks, all the RIGHT socks, or 1 ANY sock; whichever
of these 3 options is the largest is the worst case for that sock.

(n.b. the option for ANY is either 0 or 1, i.e. if you have 183 ANY socks then worst case is you pick 1 since 2 is guaranteed a pair)

For left and right e.g. 8, 1325 then worst case is that you pick all 1325 right socks without picking a single left
so you are comparing max(right, left, 0 or 1 depending if any > 0) for each sock type

The overall result is the sum of these worst cases per sock type, summed over all sock types (since worst cases are independent)
then need to add +1, to get the smallest number to be guaranteed one pair.

CARE!: Also you need to check that the pairings ACTUALLY EXIST SOMEWHERE ALSO
i.e. you need to find at least one sock type that has either >= 1 left AND 1 right or >= 2 ANY's.
Once you do, you know that a solution is possible - so, in my implementation, I track this with a flag Boolean variable
"""
n = int(input())

d = {}
for _ in range(n):
    name, loc, val = input().split()
    
    if name not in d:
        d[name] = [0, 0, 0]

    val = int(val)
    if loc == "left":
        i = 0
    elif loc == "right":
        i = 1
    else:
        i = 2

    d[name][i] += val

possible = False
res = 0
for k, v in d.items():
    if (v[2] >= 2) or (v[0] >= 1 and v[1] >= 1):
        possible = True
    # See notes above: this is "0 or 1 depending if any > 0"
    #                                VVVVVVVV
    worst_case = max(v[0], v[1], int(v[2] > 0))
    res += worst_case

if possible:
    print(res + 1)
else:
    print("impossible")