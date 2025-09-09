# The End of the World
# https://open.kattis.com/problems/endoftheworld
# TAGS: recursion, nice
# CP4: 0, Not In List Yet
# NOTES:
"""
I wrote a detailed solution:

https://github.com/benjaminzwhite/kattis/blob/main/detailed_solutions/endoftheworld.md
"""
while True:
    s = input()
    if s == 'X':
        break

    stk = list(s)

    REF = "ABC"
    start, target, temp = 0, 1, 2

    res = 0
    while stk:
        largest_disk = stk.pop()
        if largest_disk == REF[target]:
            # -- dont need to do any moves to get current largest disk into the right final position.
            # -- next largest disk is either at bottom of "temp" and needs to be moved to "target" using "start" as its temp pylon, 
            #    or is also at target already.
            start, temp = temp, start
        else:
            # "solve" the system above this largest disk:
            # there are "n-1" remaining disks (i.e. those remaining in stk[] ) that are being moved around and 
            # from the perspective of this largest disk it is *as if they have as their final target, the current TEMP pylon*
            # these moves will be added in next step of while loop, as long as you account for different target by taking:
            temp, target = target, temp
            # once they reach this, there will need to be added the moves for this current largest disk (so account for them NOW):
            # -- 1 move to move curr largest to curr target
            # -- 2**(n-1) - 1 moves to "solve tower of Hanoi" for the disks once they also reach the base case of being all on one pylon
            res += 1 + 2**len(stk) - 1 # this is just: 2**(n-1) of course, but left like this for clarify from notes

    print(res)