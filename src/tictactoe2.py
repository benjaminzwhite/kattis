# Tic Tac Toe
# https://open.kattis.com/problems/tictactoe2
# TAGS: brute force, improve
# CP4: 1.6d, Game (Others), Harder
# NOTES:
"""
Question asks whether a given input can ever appear as a board state in a valid game of tic tac toe:

I solved via brute force to see if solution passes:
I generate all games / valid sequences of moves and lookup each testcase if it is valid, doesn't time out.

TODO: IMPROVE: can resolve using checking-based approach, and improve implementation also (e.g. define some structs so don't have 0/1 everywhere).
"""
from collections import deque
from copy import deepcopy

valid = set()

# board_representation, then player number either 0 or 1.
q = deque(
	[(
		[['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']], 0
		)
	])

while q:
    board, player = q.popleft()

    curr = ''.join(x for row in board for x in row)
    if curr in valid:
        continue
    
    valid.add(curr)

    finished = False
    for row in board:
        if row == ['X', 'X', 'X'] or row == ['O', 'O', 'O']:
            finished = True
    for col in zip(*board):
        if col == ('X', 'X', 'X') or col == ('O', 'O', 'O'):
            finished = True
    if (board[0][0] == board[1][1] == board[2][2] == 'X') or (board[0][0] == board[1][1] == board[2][2] == 'O'):
        finished = True
    if (board[2][0] == board[1][1] == board[0][2] == 'X') or (board[2][0] == board[1][1] == board[0][2] == 'O'):
        finished = True

    if not finished: # if current player didn't win, then board can support another move, by player [CARE! since I init with player = 0 and empty board, it is player 0 who goes first on empty board [since empty board does NOT trigger Finished boolean] -> so need player=0 to be 'X']
        for r in range(3):
            for c in range(3):
                if board[r][c] == '.':
                    tmp = deepcopy(board)
                    tmp[r][c] = 'X' if player == 0 else 'O'
                    q.append(
                    	(tmp, 1 - player)
                    	)


N = int(input())
for casenumber in range(1, N + 1):
    testcase = [input() for _ in range(3)]
    
    if casenumber < N: # emptylines between cases but not at end -.-
        input()

    conv = ''.join(x for row in testcase for x in row)
    if conv in valid:
        print("yes")
    else:
        print("no")