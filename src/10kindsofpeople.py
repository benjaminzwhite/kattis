# 10 Kinds of People
# https://open.kattis.com/problems/10kindsofpeople
# TAGS: flood fill, grid, improve
# CP4: 4.2c, Flood Fill, Harder
# NOTES:
"""
TODO: IMPROVE: my implementation is not good and almost gets TLE.

I guess I need to improve my flood fill code in general, as here I only flood fill once; also used R*C regions array rather than a dict{}
as the latter approach TLE (adding millions of items [(curr_r,curr_c)] = curr_region_id to a dict seems to be slow) so not sure where else
I can optimize further apart from the core flood fill logic.

---

Note that queries are 1-based indexed so I work throughout with real BOARD INDICES 0 based but for queries, you
have to remember to take the inputs and -1 them to align with board/results obtained
"""
R, C = map(int, input().split())
board = []
for _ in range(R):
    board.append(input())

curr_region_id = 1 # will assign a dummy number to every new region that we flood fill, increment by 1 after each flood filld
MOVES = [(1, 0), (-1, 0), (0, 1), (0, -1)]
seen = set()
regions = [[0] * C for _ in range(R)]

# -- Preprocess (flood fill once) --
for r in range(R):
    for c in range(C):
        if (r, c) in seen:
            continue
        
        TYPE = board[r][c] # either '1' or '0'
        stk = [(r, c)]
        
        while stk:
            curr_r, curr_c = stk.pop()
            seen.add((curr_r, curr_c))
            regions[curr_r][curr_c] = curr_region_id
            
            for dr, dc in MOVES:
                if 0 <= (r_ := curr_r + dr) < R and 0 <= (c_ := curr_c + dc) < C and (r_, c_) not in seen and board[r_][c_] == TYPE:
                    stk.append((r_, c_))
        
        curr_region_id += 1

# -- Queries --
Q = int(input()) # num queries

for _ in range(Q):
    start_r, start_c, end_r, end_c = map(int, input().split())
    start_r -= 1
    start_c -= 1
    end_r -= 1
    end_c -= 1
    if regions[start_r][start_c] == regions[end_r][end_c]:
        # start and end in same region, so get type 0/1:
        if board[start_r][start_c] == '1':
            print("decimal")
        else:
            print("binary")
    else:
        # start and end NOT in same region
        print("neither")