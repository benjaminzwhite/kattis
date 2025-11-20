# Terraces
# https://open.kattis.com/problems/terraces
# TAGS: graph, DFS, grid
# CP4: 4.2a, Finding CCs
# NOTES:
C, R = map(int, input().split())

board = []
for _ in range(R):
    board.append(list(map(int, input().split())))

seen = [[0] * C for _ in range(R)]
res = 0
MOVES = [(0, 1), (1, 0), (-1, 0), (0, -1)]

queries = [(0, 0)]
while queries:
    sr, sc = queries.pop()
    curr_val = board[sr][sc] 
    stk = [(sr, sc)]
    curr_area = 0
    ok = True
    while stk:
        r, c = stk.pop()
        if seen[r][c]:
            continue
        seen[r][c] = 1
        curr_area += 1
        for dr, dc in MOVES:
            if 0 <= (r_ := r + dr) < R and 0 <= (c_ := c + dc) < C:
                if board[r_][c_] == curr_val:
                    stk.append((r_, c_))
                else:
                    if board[r_][c_] < curr_val:
                        ok = False
                    queries.append((r_, c_))
    if ok:
        res += curr_area

print(res)
