# Frogger
# https://open.kattis.com/problems/frogger
# TAGS: BFS, nice
# CP4: 0, Not In List Yet
# NOTES:
"""
I wrote a detailed solution:

https://github.com/benjaminzwhite/kattis/blob/main/detailed_solutions/frogger.md
"""
from collections import deque

T = int(input())
for _ in range(T):
    
    max_rounds = int(input())
    
    R, C = map(int, input().split())
    board = [input() for _ in range(R + 2)]
    
    # SEEN is a bit more complex than a usual set() -> the system is PERIODIC so if we have visited a cell r,c at an equivalent time (modulo period)
    # then we have already "been" in this configuration so will skip adding it to the BFS
    PERIODICITY = C
    SEEN = [[[0] * C for _ in range(R + 2)] for _ in range(PERIODICITY)] 

    start_c = board[-1].index('F')
    end_c = board[0].index('G')

    MOVES = [(0, 0), (1, 0), (0, 1), (-1, 0), (0, -1)] # CARE!!! 5 moves since you CAN STAND STILL SO 0,0 VALID

    q = deque([(0, R + 1, start_c)]) # q: (num_rounds, r, c) 

    reached = False
    while q:
        num_rounds, r, c = q.popleft()

        if num_rounds > max_rounds:
            continue

        if r == 0 and c == end_c:
            reached = True
            res = num_rounds
            break

        if SEEN[num_rounds % PERIODICITY][r][c]:
            continue
        SEEN[num_rounds % PERIODICITY][r][c] = 1

        for dr, dc in MOVES:
            if 0 <= (r_ := r + dr) < R + 2 and 0 <= (c_ := c + dc) < C:
                
                t_ = num_rounds + 1
                cprime = (c_ + t_ % C) % C
                if (r_ % 2 == R % 2 and board[r_][c_ - t_ % C] == 'X') or (r_ % 2 != R % 2 and board[r_][cprime] == 'X'):
                    continue

                q.append((t_, r_, c_))

    if reached:
        print(f"The minimum number of turns is {res}.")
    else:
        print("The problem has no solution.")