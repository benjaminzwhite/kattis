# Robotopia
# https://open.kattis.com/problems/robotopia
# TAGS: brute force
# CP4: 3.2k, Math Simulation, H
# NOTES:
"""
I think it is overranked, at red, because people must be making the same mistake I did on first submission: 
it's just reading comprehension (without a supporting test case that illustrates this behaviour though)
==> YOU ARE NOT ALLOWED 0 OF EITHER ROBOT, so the r1, r2 MUST BE >= 1.

Therefore if e.g. the "mathematics solution" is [(2,3), (0,10), (738,0)] then although this corresponds therefore to "multiple solutions"
it is, for this exercise, considered IN FACT A "VALID UNIQUE SOL" since there is only one pair - (2,3) - with nonzero entries.

CARE! you also need to check, after doing the // integer division that the remainder is 0 also
(otherwise will get false positives due to rounding behavior i.e. will ignore the leftovers
and assume e.g. that 16//5 = 3 is a good solution for the number of robots r2)
"""
N = int(input())
for _ in range(N):
    l, a, ll, aa, L, A = map(int, input().split())

    res= []
    for r1 in range(1, L // l + 1):
    	delta_l = L - r1 * l
    	delta_a = A - r1 * a
    	r2 = delta_l // ll
        if r2 == (delta_a // aa) and r2 > 0 and (delta_l % ll == 0) and (delta_a % aa == 0):
            res.append((r1, r2))

    if len(res) == 1:
        print(*res[0])
    else:
        print('?')