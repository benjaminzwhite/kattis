# Bungee Builder
# https://open.kattis.com/problems/bungeebuilder
# TAGS: array, logic, nice
# CP4: 2.2k, Stack-based Problems
# NOTES:
"""
Nice exercise:
found the clever insight when I stated out loud the "non overlapping subproblem" property (solution is obvious after)
i.e. explicitly observed and stated "When x > highest_peak, all prior x-values are inaccessible/irrelevant so you can reset the problem data."
This naturally allows you to then work out the other case, and how to handle the valley behavior
(idea of "transparent ghosts" is often useful in these kind of exercises, see comments below)
"""
n = int(input())

xs = map(int, input().split())

highest_peak = -float('inf')
lowest_valley = float('inf')
res = 0

for x in xs:
    if x > highest_peak:
        # All the x's to the left of this peak are inaccesible now, so essentialy start a new subproblem from this point x.
        # We can realise any jump between this new peak and the previous highest peak; the height of the jump is constrained
        # by min(x, highest_peak) which is always going to be: highest_peak (because we are in this if-statement: x > highest_peak )
        res = max(res, highest_peak - lowest_valley)
        highest_peak = x
        lowest_valley = float('inf')
    else:
        # if x <= highest_peak then we are somewhere to the right of our current highest_peak
        # so we update our lowest_valley, if applicable:
        lowest_valley = min(lowest_valley, x)
        # then we can imagine that all the values between the current lowest_valley and the current value of x are "transparent ghosts":
        # e.g. imagine:
        # [100, 13, >>2<<, 8, 10, 11, >>5<<, ...]
        # when we reach x=5, lowest_valley will be =2, and we compute the jump height value "5 - 2" EVEN THOUGH THIS JUMP IS NOT POSSIBLE
        # why can we do this? why doesn't it mess up the "real" answer?
        # -> because, IF ANY JUMP IS NOT POSSIBLE, it is precisely because there is at least one LARGER X-VALUE PRIOR TO x=5 THAT BLOCKS IT
        # -> BUT THIS/THESE LARGER VALUE(S) (here: 8, 10, 11) WILL HAVE ALREADY BEEN COMPUTED AND ITS/THEIR (real, physically possible) CORRESPONDING HEIGHT 
        # WILL HAVE BEEN RECORDED.
        # e.g. for [...2,8,10,11,5,...] we will have found "real, actual" heights 8-2=6,10-2=8,11-2=9, so that then when we compute 
        # the "unphysical/impossible" 5-2 = 3 it is < 9 so WILL NEVER be stored when we take max(res,x - lowest_valley) so we're ok
        res = max(res, x - lowest_valley)

print(res)