# Rings
# https://open.kattis.com/problems/rings2
# TAGS: grid, bfs
# CP4: 2.2d, 2D Array, Harder
# NOTES:
"""
Kind of a 2d BFS/flood fill exercise.

Implementation notes:

Start by processing input board[] and track:
a) all cells that are '.' and assign them distance = 0 in the dist[][] array
b) all BOUNDARY CELLS THAT ARE TREES i.e. cell == 'T' and r=0 or R-1 / c=0 or C-1 and assign them distance = 1

The clever trick is, now you will process a curr_q which contains the current distance being treated, and assign curr+1 to all neighboring cells
that have not been updated (i.e that are still -1 initialized value)

Clever approach: if you do it naively and append a) b) BOTH TO SAME initial q, you get problems as if you process a dist=1 element before a dist=0 element from original board
you can end up assigning values like d=1+1 = 2 to a cell that could be reached from a d=0 i.e. -> 0+1 = 1 distance cell

So my approach is to build initial curr_q in order of 0-dists FIRST, then 1-dists; both obtained from initial board, then process curr_q, each time
creating a next_q which stores all the values that have been updated from -1 from locations in the curr_q
Then finally, set curr_q = next_q and repeat (now all the cells will be those at distance +1 etc etc)
"""
R, C = map(int, input().split())

board = []
for _ in range(R):
    board.append(input())

dist = [[-1] * C for _ in range(R)]
MOVES = [(-1, 0), (1, 0), (0, 1), (0, -1)]

zero_dist = []
one_dist = []
for r, row in enumerate(board):
    for c, cell in enumerate(row):
        if cell == '.':
            dist[r][c] = 0
            zero_dist.append((r, c))
        elif cell == 'T' and r in (0, R - 1) or c in (0, C - 1):
            dist[r][c] = 1 # these the are tree cells that touch "wall"/boundary of board
            one_dist.append((r, c))

max_dist = 0
# IMPLEMENTATION NOTES: this is the "clever bit" that avoids exotic data structures O_o
# handle all 0's first, avoids bad behavior with 1's assigning distance 2 to a cell that could in principle be reached 
# by a 0 (but that occurs "later" in the R,C board for ex [T,T,T][0,0,0] would assign [1,2,1] to first row but in fact 
# should be [1,1,1] due to the 0 beneath etc - the given R,C=6,6 testcase was failing for this reason for me if i just 
# made 1 big curr_q in the code above, instead of zero_dist and one_dist separately, directly while processing inputs)
curr_q = zero_dist + one_dist
while curr_q:
    next_q = []
    for r, c in curr_q:
        for dr, dc in MOVES:
            if 0 <= (r_ := r + dr) < R and 0 <= (c_ := c + dc) < C and dist[r_][c_] < 0:
                dist[r_][c_] = dist[r][c] + 1
                max_dist = max(max_dist, dist[r_][c_])
                next_q.append((r_, c_))
    curr_q = next_q

# output formatting requirement
# wants for double digit results to have 3 spaces i.e. .6,.2,.9
# but if there is a 10,11,etc in the final res, you should output ..6,..2,.10,.11 etc
for row in dist:
    print(''.join(str(x if x > 0 else '.').rjust(2 + (max_dist > 9), '.') for x in row))