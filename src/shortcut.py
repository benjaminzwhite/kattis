# Divisibility Shortcut
# https://open.kattis.com/problems/shortcut
# TAGS: mathematics, number theory, proof
# CP4: 5.3k, Divisibility Test
# NOTES:
"""
I wrote a detailed solution:

https://github.com/benjaminzwhite/kattis/blob/main/detailed_solutions/shortcut.md
"""
T = int(input())
for _ in range(T):
    b, k = map(int, input().split())

    bb = b - 1
    res = 1

    for d in range(1, int(bb**0.5) + 1):
        if bb % d == 0:
            q = bb // d

            # since d is increasing, bb//d is decreasing from max possible value so 
            # the FIRST q <= k you encounter, if any, is best possible answer
            if q <= k: 
                res = q
                break
            if d > k:
                break
            res = max(res, d)
    
    print(res)