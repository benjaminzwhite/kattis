# Bootstrapping Number
# https://open.kattis.com/problems/bootstrappingnumber
# TAGS: binary search
# CP4: 3.3b, Bisection and BSTA, E
# NOTES:
"""
I repeat the binary search until the values of l and r are within EPS of eachother (avoids infinite loop TLE risk
for this kind of exercise, since floats are involved etc.)
"""
EPS = 1e-9 # adjusted until the error in the resulting x is < 1e-6

n = int(input())

l, r = EPS, 11 # 1**1 = 1 which is N_MIN; 10**10 = 10_000_000_000 which is N_MAX

while abs(l - r) > EPS:
    mid = (l + r) / 2
    bs_n = mid**mid
    if bs_n > n:
        r = mid
    else:
        l = mid

print(mid)