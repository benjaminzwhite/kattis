# Chess
# https://open.kattis.com/problems/chess
# TAGS: brute force, improve
# CP4: 1.6b, Game (Chess)
# NOTES:
"""
TODO: IMPROVE - I'm sure you can implement this better.

Note that there can be 2 intersection points between the 2 pieces:
Consider e.g. a piece on row 0 and col 3 , and other piece on row 2 and col 3 -> paths intersect at row 1 col 2 and row 1 col 4.

So, with implementation below:
- check first if the target is reachable in 1 move from current location (ie on same diagonal)
- then and only then consider whether there is NONZERO intersection between the 2 pieces' diagonals
"""
T = int(input())

ROWS = "87654321"
COLS = "ABCDEFGH"
MOVES = [(dr, dc) for dr in (-1, 1) for dc in (-1, 1)]

for _ in range(T):
    curr_c, curr_r, target_c, target_r = input().split()
    if (curr_c, curr_r) == (target_c, target_r):
        print(f"0 {curr_c} {curr_r}")
        continue
    
    from_curr, from_target = set(), set()
    
    cc = COLS.index(curr_c)
    cr = ROWS.index(curr_r)
    tc = COLS.index(target_c)
    tr = ROWS.index(target_r)
    
    def process(c, r, from_set):
        for move in MOVES:
            dr, dc = move
            for k in range(8):
                dr_, dc_ = k * dr, k * dc
                r_, c_ = r + dr_, c + dc_
                if (0 <= r_ < 8) and (0 <= c_ < 8):
                    from_set.add((c_, r_))
    
    process(cc, cr, from_curr)
    
    # CASE WHERE TARGET IS ON SAME DIAGONAL AS THE CURRENT PIECE
    if (tc, tr) in from_curr:
        print(f"1 {curr_c} {curr_r} {target_c} {target_r}")
        continue
    
    process(tc, tr, from_target)
    
    res = list(from_curr.intersection(from_target)) # update - could just pop from set instead of converting to list and taking res[0] see below.
    
    # CASE WHERE TARGET NOT ON SAME DIAGONAL - EITHER THE DIAGONALS:
    # A) do not intersect -> Impossible to move from curr to target
    if not res:
        print("Impossible")
    # B) do intersect -> pick any valid intersection coordinates, here res[0] for convenience, then move from curr->intersection->target in 2 moves
    else:
        coords = res[0]
        print(f"2 {curr_c} {curr_r} {COLS[coords[0]]} {ROWS[coords[1]]} {target_c} {target_r}")