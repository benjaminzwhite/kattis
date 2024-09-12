# Flow Shop
# https://open.kattis.com/problems/flowshop
# TAGS: grid, dynamic programming
# CP4: 2.2c, 2D Array, Easier
# NOTES:
"""
Not sure I understand 100% what it's asking:
but noticed that the solutions are basically lattice paths from top left to "bottom right" on
a row by row basis, where you take the MAX of (above_cell, left_cell) and add it to current cell

-> implemented with a O(2m) dp rather than O(n*m) by just tracking the current and previous dp values instead of the entire n*m board

-> row result is the last value in each row (here curr[-1]) this corresponds to the total time taken
to assemble the whatever_it_is_thing we are assembling, so just need to append that value while processing
online, then can overwrite the array and dont need to store it
"""
N, M = map(int, input().split())

res = []
prev = [0] * M # dp array of previous row

for _ in range(N):
    curr = [0] * M
    row = map(int, input().split())
    for i, cell in enumerate(row):
        if i == 0:
            curr[i] = cell + prev[i] # no cell to the left, so only add the value from above
        else:
            curr[i] = cell + max(prev[i], curr[i-1])
    res.append(curr[-1])
    prev = curr
    
print(' '.join(map(str, res)))