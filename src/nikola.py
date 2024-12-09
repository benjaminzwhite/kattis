# Nikola
# https://open.kattis.com/problems/nikola
# TAGS: dynamic programming
# CP4: 3.5f, DP level 1
# NOTES:
"""
The recursive solution times out TLE after at 5th test case - I left it below for reference.

Dynamic programming states explanations are in main code.

---

from functools import lru_cache

N = int(input())

xs = []

for _ in range(N):
    xs.append(int(input()))
    
def nikola(xs):
    @lru_cache
    def helper(idx, prev_jump):
        if idx == len(xs) - 1:
            return xs[idx]
        if idx < 0 or idx >= len(xs):
            return float('inf')

        jump_right = xs[idx] + helper(idx + prev_jump + 1, prev_jump + 1)
        jump_left = xs[idx] + helper(idx - prev_jump, prev_jump)

        return min(jump_left, jump_right)

    return helper(1, 1)

print(nikola(xs))
"""
N_squares = int(input())

xs = []
for _ in range(N_squares):
    xs.append(int(input()))

IMPOSSIBLE = float('inf')
dp = [[IMPOSSIBLE] * N_squares for _ in range(N_squares + 1)] # dummy row due to 1 based indexing on the xs

# Base case:
# if you are on the last square, regardless of jump size, it always costs xs[-1] to "reach" the last/Nth square, with 0 jumping required
for row in range(N_squares + 1):
    dp[row][-1] = xs[-1]

# Recursive case - working backwards from end state
for jump_size in range(N_squares - 1, 0, -1):
    for square_idx in range(N_squares - 1): # <- -1 because don't update last square
        # if can reach a forward square with a single forward jump from this square_idx, then cost is xs[square_idx] + forward square cost
        fwd_idx = square_idx + jump_size
        if fwd_idx < N_squares and (dp[jump_size + 1][fwd_idx] != IMPOSSIBLE): # <--- check that dp[jump_size+1][fwd_idx] is known to reach final square with LARGER jumps
            dp[jump_size][square_idx] = xs[square_idx] + dp[jump_size + 1][fwd_idx]

        # we must also update squares which can do 2 jumps: 
        # a backward jump of size jump-1 then a subsequent one of size jump 
        # Since we process in DECREASING order of jump size, THE LATTER OF WHICH HAS BEEN TREATED EARLIER IN THE BOTTOM UP RECURSION
        back_idx = square_idx - (jump_size - 1)
        if back_idx >= 0:
            # Update square with the back jump option - either for the first time (if it is currently IMPOSS) or take min of existing value:
            dp[jump_size][square_idx] = min(dp[jump_size][square_idx], xs[square_idx] + dp[jump_size][back_idx])

# the result is the value of the start state which is: 2nd square i.e. square_index 1 (CARE! indexing off by 1 errors!) with the jump_size of +2
# so this is stored in dp[2][1]
print(dp[2][1])