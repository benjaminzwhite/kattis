# Tetris Generation
# https://open.kattis.com/problems/tetrisgeneration
# TAGS: brute force, string
# CP4: 0, Not In List Yet
# NOTES:
"""
Just checking if any of the 7 choices of breaking the string "abc|defghik|lm"... with | defining chunks of size 7
leads to all chunks having 0 repeated letters. If so, this is a valid subdivision and therefore could be produced by Tetris
"""
T = int(input())
for _ in range(T):
    s = input()
    F = 0
    for offset in range(1, 8):
        l = 0
        r = offset
        ok = True
        while l < len(s):
            if len(set(s[l : r])) != len(s[l : r]):
                ok = False
                break
            l = r
            r += 7
        if ok:
            F = 1
            break
    print(F)