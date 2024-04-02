# Rotate and Cut
# https://open.kattis.com/problems/rotatecut
# TAGS: logic
# CP4: 6.2f, Really Ad Hoc
# NOTES:
"""
Reading comprehension: hard to understand - in fact there's no "rotation", just imagine you are removing from front and end of string in turn.

The N-max is huge 10**9 but the len(s) max is 2000 -> it takes at most ~ 30 steps to reduce 2000 to len 3 by taking *= 3/4
and once you have a string of length 3, taking the operation "remove floor(1/4 of chars)" removes floor(3/4) = 0 chars on subsequent steps.
"""
from math import floor

T = int(input())

for _ in range(T):
    n, s = input().split()
    n = int(n)
    l, r = 0, len(s) - 1
    
    front = 1 # due to the wording about "rotating" on the first step you "flip the word and remove from the end" which is basically removing THE FRONT OF THE WORD
    while r - l > 2 and n: # since max(len(s)) = 2000 takes at most ~ 30 steps to reduce to length 1 by *= 3/4 each step. Can stop once reach a string of length 3 !!! NOT 1!!! SINCE once yu have 3 or fewer chars, floor (len/4) == 0 so dont remove anything else subsequently
        n -= 1
        if front:
            l += floor((r - l + 1) / 4)
        else:
            r -= floor((r - l + 1) / 4)
        front = 1 - front

    print(s[l:r + 1])