# Nered
# https://open.kattis.com/problems/nered
# TAGS: array, range sum, improve
# CP4: 3.5a, Max 1D/2D Range Sum
# NOTES:
"""
TODO: IMPROVE: Try to improve/redesign the implementation, not sure if there are simpler ways to build the prefix sums array instead of the
3 times i,j loops over range(N) etc.

---

Notice that since we have always the needed number M of rectangles, IT DOESN'T MATTER HOW THEY ARE PILED UP, just their footprint, since it will
always take 1 move per cube that is out of place, to fill in 1 empty square in the final rectangle.
So if all the surplus ones are on top of the same cube, it makes no difference.

So use 2d rectangle range sum to find the maximum FLOOR AREA/FOOTPRINT of the colums of cubes on the NxN grid
Using prefix sums approach; THEN ONCE YOU HAVE THE PREFIX SUMS, YOU NEED TO QUERY "ALL RECTANGLES IN THE NxN GRID"

-> But you can simplify, don't need to check ALL possible rectangles but only those whose dimensions:
a) contain exactly M cubes and
b) fit inside the NxN board

-> So factorize M e.g. 10 = 1,10 / 2,5 / 5,2 / 10,1: these are the 4 "queries" to perform for each TOP,LEFT location in the prefix sum dp array
In other words, starting at r,c = 0,0 as top left, you prefix sum query all these 4 rectangles from that top left location, and see what the 
floor footprint area is for each of the rectangles then repeat for r,c = 0,1 / 0,2 /.... / N,N

---

Implementation note:

Prefix sum stuff is tricky due to N+1 rows and columns (due to "padding" approach to handle the indexes - basically CARE! for off by one errors O_o)
"""
N, M = map(int, input().split())

board = [[0] * N for _ in range(N)]

for _ in range(M):
    r, c = map(int, input().split())
    # NOTES: just assign 1 to the given location - 1 means that there is a column OF ANY HEIGHT (might have 2,3,100 squares on top of it) -> we are only interested in the rectangle "footprint" since we know there will be enough squares to move around to fill in the gaps
    board[r - 1][c - 1] = 1 # CARE! 1-BASED INDEXING

prefix_sums = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(N):
    for j in range(N):
        prefix_sums[i + 1][j + 1] += board[i][j]

for i in range(N):
    for j in range(N):
        prefix_sums[i + 1][j + 1] += prefix_sums[i][j + 1] 

for i in range(N):
    for j in range(N):
        prefix_sums[i + 1][j + 1] += prefix_sums[i + 1][j] 

# Factorize M into (M//d, d) as these are the only possible rectangle sizes that can comprise a total of M squares
possible_rectangles = set()
for d in range(1, int(M**0.5) + 1):
    if M % d == 0:
        possible_rectangles.add((M // d, d))
        possible_rectangles.add((d, M // d))

# queries: range over all possible top,left in range N,N
max_area_covered = 0
for top in range(N):
    for left in range(N):
        for dr, dc in possible_rectangles:
            # need to ensure that the current rectangle will fit entirely within the NxN board
            # NOTE: since we are looking within the prefix sum array which has a padding row and col, we check for r,c <=N instead of <N !!!
            if (bottom := top + dr) <= N and (right := left + dc) <= N:
                curr_area_covered = prefix_sums[bottom][right] - prefix_sums[bottom][left] - prefix_sums[top][right] + prefix_sums[top][left]
                max_area_covered = max(max_area_covered, curr_area_covered)

# largest number of squares covered by any possible rectangle is max_area_covered
# so the result is that we need to move at least M - max_area_covered squares into that rectangle to turn it into a full rectangle of squares
res = M - max_area_covered

print(res)