# Eight Queens
# https://open.kattis.com/problems/8queens
# TAGS: array, grid
# CP4: 3.2b, Iterative (Two Loops)
# NOTES:
"""
Not all testcases have 8 queens, so have to check for it in addition to board checker logic.

Could use a covered[][] 8x8 array instead of a set() for tracking covered positions, but the benefit of
using set() is that you can update very easily with range(-8,8).
This works because the "unphysical" locations, i.e. outside of the real board, that thereby get added 
to covered() will not be checked by (r,c) at any step, e.g. (-7,5) location will never correspond to a real (r,c)
"""
board = [input() for _ in range(8)]

covered = set()
ok = True
cnt = 0

for r, row in enumerate(board):
    for c, cell in enumerate(row):
        if cell == '*':
            cnt += 1
            if (r, c) in covered:
                ok = False
                break
            covered.update({(r, i) for i in range(8)})
            covered.update({(i, c) for i in range(8)})
            covered.update({(r + i, c + i) for i in range(-8, 8)})
            covered.update({(r - i, c + i) for i in range(-8, 8)})

# CARE! Need to also check there are 8 queens
if ok and cnt == 8:
    print("valid")
else:
    print("invalid")

