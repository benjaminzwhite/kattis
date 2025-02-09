# Burizon Fort
# https://open.kattis.com/problems/burizonfort
# TAGS: logic, mathematics, array, nice
# CP4: 0, Not In List Yet
# NOTES:
"""
I wrote a detailed solution:

https://github.com/benjaminzwhite/kattis/blob/main/detailed_solutions/burizonfort.md
"""
T = int(input())

for _ in range(T):
    m = int(input())
    divisors = set()
    d = 1
    while d * d <= m:
        if m % d == 0:
            divisors.update({d, m // d})
        d += 1
    divisors = sorted(divisors)

    # using variable names from detailed notes, see link above
    ok = True
    prev_S = 0
    for curr_D in divisors:
        if curr_D <= prev_S + 1:
            prev_S += curr_D
        else:
            ok = False
            break

    if ok:
        print("Yes")
    else:
        print("No")