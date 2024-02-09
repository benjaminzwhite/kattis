# Espresso Bucks
# https://open.kattis.com/problems/espressobucks
# TAGS: grid, greedy
# CP4: 9.cons, Construction
# NOTES:
"""
Basically "local/greedy" approach works: place a shop on each cell that you can as you move through the grid.

---

Note that this solution produces configurations with MORE THAN the "optimal" number of stores, but it still is accepted.

For example: the test case shown on exercise has 23 shops 'E' but my solution places 25 shops for this test case.

Both satisfy the exercise conditions but the test case shown one is "more optimal".
"""
MOVES = [(-1, 0), (1, 0), (0, 1), (0, -1)]

R, C = map(int, input().split())
board = [list(input()) for _ in range(R)]

for r, row in enumerate(board):
	for c, cell in enumerate(row):
		if cell == '.':
			if all(board[r_][c_] != 'E' for dr, dc in MOVES if 0 <= (r_ := r + dr) < R and 0 <= (c_ := c + dc) < C):
				board[r][c] = 'E'

for x in board:
	print(''.join(x))