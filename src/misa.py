# Misa
# https://open.kattis.com/problems/misa
# TAGS: grid
# CP4: 3.2d, Three+ Nested Loops, H
# NOTES:
"""
As you move through board and count neighboring cells containing 'o' you either:

    1) increase the total number of adjacents by this count, if current cell is == 'o' (so this person is handshaking all adjacents)

 or 2) if this cell is not 'o' i.e. is EMPTY, then it is a possible insertion point for 1 new extra person, so store the max 
       adjacents belonging to an empty cell

Final result is adjacents // 2 (since we double counted handshakes) plus max_extra_handshakes; the max value of the adjacents
over all inidivual emtpy cells from step 2)
"""
R, C = map(int, input().split())

board = []
for _ in range(R):
    board.append(input())

MOVES = [(dr, dc) for dr in (-1, 0, 1) for dc in (-1, 0, 1) if (dr or dc)]
adjacents = 0
max_extra_handshakes = 0

for r, row in enumerate(board):
    for c, cell in enumerate(row):
        adjs = 0
        for (dr, dc) in MOVES:
            if 0 <= (r_ := r + dr) < R and 0 <= (c_ := c + dc) < C and board[r_][c_] == 'o':
                adjs += 1
        if cell == 'o':
            adjacents += adjs
        else:
            max_extra_handshakes = max(max_extra_handshakes, adjs)

res = adjacents // 2 + max_extra_handshakes
print(res)