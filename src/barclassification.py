# Bar Classification
# https://open.kattis.com/problems/barclassification
# TAGS: array, grid
# CP4: 0, Not In List Yet
# NOTES:
"""
Should be self explanatory below:

For each row (same argument for column) check that:
the count of the NOT-1-CELLS == (N - curr_row_count),  
plus the count of all 1's that are NOT IN THIS ROW == (total_ones - curr_row_count)
is <= N.

If so this current row is consistent with the requirement that it was originally fully 1's then <= N cells were toggled on the board.
"""
N = int(input())

board = []
for _ in range(N):
    board.append(input())

horiz = False
vert = False

ones = 0
row_counts = []
col_counts = [0] * N
for row in board:
    curr = 0
    for i, cell in enumerate(row):
        if cell == '1':
            curr += 1
            col_counts[i] += 1
    row_counts.append(curr)
    ones += curr

for rc in row_counts:
    if (N - rc) + (ones - rc) <= N:
        #print("OK row for row count", rc)
        horiz = True

for cc in col_counts:
    if (N - cc) + (ones - cc) <= N:
        #print("OK col for col count: ",cc)
        vert = True

if horiz and vert:
    print('+')
elif horiz:
    print('-')
else:
    print('|')