# Flip Five
# https://open.kattis.com/problems/flipfive
# TAGS: BFS, bitmask, nice
# CP4: 8.2b, State-Space, BFS, E
# NOTES:
"""
Nice little practice with bitmask and encoding states.

Left comments, but basically:
- the moves can be encoded as binary numbers representing the mask on the board
- you XOR each mask with the current state to get the new state
"""
from collections import deque

P = int(input())

for _ in range(P):
    inps = [input() for _ in range(3)]
    # converts 3x3 grid of * and . into the corresponding binary number then into correspnding integer
    target_state = int(''.join(inps).replace('*', '1').replace('.', '0'), 2)

    seen = set()
    # initial state is all cells 0/white -> encode as binary 000_000_000 = 0 as int
    q = deque([(0, 0)]) # CURR_STATE, CURR_MOVES

    # make a list of the 9 keypresses here as binary numbers
    # made explicit variable names here to see clearly which is which
    top_left = int('110100000', 2)
    top_centre = int('111010000', 2)
    top_right = int('011001000', 2)
    mid_left = int('100110100', 2)
    mid_centre = int('010111010', 2)
    mid_right = int('001011001', 2)
    bot_left = int('000100110', 2)
    bot_centre = int('000010111', 2)
    bot_right = int('000001011', 2)

    MASKS = [top_left, top_centre, top_right, mid_left, mid_centre, mid_right, bot_left, bot_centre, bot_right]

    while q:
        curr_state, curr_moves = q.popleft()
        if curr_state == target_state:
            print(curr_moves)
            break
        if curr_state in seen:
            continue
        seen.add(curr_state)

        for mask in MASKS:
            next_state = curr_state
            for i in range(9): # N = 9
                if mask & (1 << i):
                    next_state ^= 1 << i
            q.append((next_state, curr_moves + 1))