# Prozor
# https://open.kattis.com/problems/prozor
# TAGS: grid, range sum, improve
# CP4: 3.5a, Max 1D/2D Range Sum
# NOTES:
"""
TODO: IMPROVE: It is ranked easy O_o Maybe I'm not seeing a simpler approach.

It's 2d max submatrix sum problem in "disguise" - instead of summing values, you sum 1 if there is a fly and 0 if not

I compute all the prefix sums once, then consider all possible squares: to determine a square take a top,left location
then find its bottom,right location via +K on row and col

---

NOTE: there's a lot of tedious +/-1 and +/-2 stuff due to the fact that you DO NOT include flies that are on the boarder of the K*K area
So essentially the square is K-2 * K-2.
Also the output wants you to output ASCII art instead of just the coordinate of e.g. top left of square, which would be a lot simpler IMHO.
"""
R, C, K = map(int, input().split())

board = []

for _ in range(R):
    board.append(list(input()))

best = -1

# IMPLEMENTAION NOTE:
# prefix_sums HAS DUMMY r=0,c=0 padding row and col to handle rectangles that start on top row or col
prefix_sums = [[0] * (C + 1) for _ in range(R + 1)]

for i in range(R):
    for j in range(C):
        prefix_sums[i + 1][j + 1] += (board[i][j] == '*') # Increase sum by 1 each time there is a fly, if not you do not increas prefix sum

for i in range(R):
    for j in range(C):
        prefix_sums[i + 1][j + 1] += prefix_sums[i][j + 1]

for i in range(R):
    for j in range(C):
        prefix_sums[i + 1][j + 1] += prefix_sums[i + 1][j]

for r in range(1, R - K + 2): # START AT r=1, c=1 since we are in prefix_sums matrix (not in the "original grid" matrix)
    for c in range(1, C - K + 2):
        top, left = r, c
        bottom, right = r + K - 2, c + K - 2 # -2 because we DO NOT include the borders
        curr_flies = prefix_sums[bottom][right] - prefix_sums[bottom][left] - prefix_sums[top][right] + prefix_sums[top][left]
        if curr_flies > best:
            best = curr_flies
            res = (r, c) # r,c is in PREFIX SUM MATRIX which has dummy row and col 0,0 so will need to perform -1,-1 for the ORIGINAL r,c in ORIGINAL BOARD

r, c = res
board_r, board_c = r - 1, c - 1

# Output formatting -.-
for row, col in [(board_r, board_c), (board_r + K - 1, board_c), (board_r, board_c + K - 1), (board_r + K - 1, board_c + K - 1)]:
    board[row][col] = '+'

for row in (board_r, board_r + K - 1):
    for col in range(board_c + 1, board_c + K - 1):
        board[row][col] = '-'

for col in (board_c, board_c + K - 1):
    for row in range(board_r + 1, board_r + K - 1):
        board[row][col] = '|'
        
print(best)
for row in board:
    print(''.join(row))