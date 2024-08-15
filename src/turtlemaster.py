# Turtle Master
# https://open.kattis.com/problems/turtlemaster
# TAGS: interpreter, grid
# CP4: 1.6d, Game (Others), Harder
# NOTES:
"""
1. board is always 8x8
2. convert each input row to a list so can modify cells (in case we need to melt ice with laser, we change I to . on board)
"""
board = []
for _ in range(8):
    row = input()
    board.append(list(row))

commands = input()

curr_r, curr_c = 7, 0 # always start at bottom left of 8x8 board
dir_idx = 0
DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)] # R will mean: increase dir_idx +1, L means decrease dir_idx -1. HANDLE WRAPAROUND WITH %.

# use i to iterate over commands, if we break early then i < len(commands) so can use as flag for last print statement
# alternative is to use e.g. a flag boolean whenever you print("Bug!") e.g. bugged = False -> True
# Could just use enumerate also, didn't go back to edit the submission.
for i in range(len(commands)):
    command = commands[i]

    if command == 'F':
        move = DIRS[dir_idx]
        dr, dc = move
        curr_r += dr
        curr_c += dc
        if (not (0 <= curr_r < 8)) or (not (0 <= curr_c < 8)) or board[curr_r][curr_c] in {'C', 'I'}:
            print("Bug!")
            break
    elif command == 'X':
        move = DIRS[dir_idx]
        dr, dc = move
        adj_r = curr_r + dr
        adj_c = curr_c + dc
        if not (0 <= adj_r < 8) or not (0 <= adj_c < 8) or board[adj_r][adj_c] != 'I':
            print("Bug!")
            break
        else:
            board[adj_r][adj_c] = '.'
    elif command == 'R':
        dir_idx = (dir_idx + 4 + 1) % 4 # there are 4 commands in DIRS list, so use % to handle wraparound
    elif command == 'L':
        dir_idx = (dir_idx + 4 - 1) % 4
    
    i += 1

# If we reach here and i == len(commands) then we did not break early, so check if we finished on the D square.
if i == len(commands):
    print("Diamond!" if board[curr_r][curr_c] == 'D' else "Bug!")