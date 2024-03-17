# Verify This, Your Majesty
# https://open.kattis.com/problems/queens
# TAGS: array
# CP4: 2.2b, 1D Array, Harder
# NOTES:
N = int(input())

avail_rows = [True] * 2 * N
avail_cols = [True] * 2 * N 
avail_up_right_diags = [True] * 2 * N
avail_up_left_diags = [True] * 2 * N

flg = True
for _ in range(N):
    r, c = map(int, input().split())
    up_right = r + c
    up_left =  r - c + N # to ensure the index in the boolean array up_left >= 0 we just add N 
    if avail_rows[r] and avail_cols[c] and avail_up_right_diags[up_right] and avail_up_left_diags[up_left]:
        avail_rows[r] = False
        avail_cols[c] = False
        avail_up_right_diags[up_right] = False
        avail_up_left_diags[up_left] = False
    else:
        flg = False
        break

if flg:
    print("CORRECT")
else:
    print("INCORRECT")