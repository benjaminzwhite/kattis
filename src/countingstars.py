# Counting Stars
# https://open.kattis.com/problems/countingstars
# TAGS: flood fill, grid, improve
# CP4: 4.2b, Flood Fill, Easier
# NOTES:
"""
TODO: IMPROVE: I don't think my implementation of flood fill is optimal in Python, need to learn improvements
"""
case = 1
while True:
    try:
        R, C = map(int, input().split())
        board = []
        for _ in range(R):
            board.append(list(input()))

        MOVES = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        def floodfill(r, c, board):
            stk = [(r, c)]
            while stk:
                r, c = stk.pop()
                board[r][c] = '#'
                for dr, dc in MOVES:
                    if 0 <= (r_ := r + dr) < R and 0 <= (c_ := c + dc) < C and board[r_][c_] == '-':
                        stk.append((r_, c_))

        regions = 0
        for r, row in enumerate(board):
            for c, cell in enumerate(row):
                if cell == '-':
                    regions += 1
                    floodfill(r, c, board)

        print(f"Case {case}: {regions}")
        case += 1
        
    except EOFError:
        break