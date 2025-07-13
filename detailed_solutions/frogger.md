# Detailed solution for Kattis - Frogger

[Problem statement on Kattis](https://open.kattis.com/problems/frogger)

It's a breadth-first search exercise, but what is interesting is how the "previously seen states" also depend not just on spatial position, but on time steps.

## Tags

BFS

## Solution

As mentioned above, the nice twist here is that I am using a "complex" `SEEN` lookup compared to other BFS exercises:

The `SEEN` is, as always, telling you which *STATES* you have visited before.

- In this exercise, the "board" is a 2d position board, but there is a 3rd dimension, **time**, which also is part of each state of the game

Interestingly in this example, the system is **periodic in this time dimension**, since e.g if each lane is of size `C`, then after `C` shifts of the position, the board is back in a previous configuration.

**So therefore for solving:** the state that you are tracking is `frog_r, frog_c, num_steps` but with the simplification that `num_steps` is measured **modulo periodicity of the game system.**

Explanation: if e.g. the `PERIODICITY` is 7, if you find yourself at `(r,c) = 5,2` at time `T = 23`, then the board itself is in the same configuration as at times `T = 23 - 7 = 16`, `16 -7 = 9`, `16 -7 = 2` etc.

So this extra dimension is the key to making the `SEEN[]` work: you can stop BFS whenever you reach a "previously reached state" with this above expanded definition of "previously reached" reflecting the periodicity in the time dimension.

### Implementation notes

**CARE!:** you are allowed to stand still, so `(0, 0)` is a valid "move" in the `MOVES` list of possible moves.

## AC code

```python
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
```