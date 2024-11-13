# Good Morning!
# https://open.kattis.com/problems/goodmorning
# TAGS: DFS, grid
# CP4: 3.2k, Backtracking (Easier)
# NOTES:
"""
Nice exercise, see comments below.

I generate all possible numbers as precompute, then for each target k, lookup if k+/- 0 is in SEEN, else +/- 1 etc. to get closest value to k
"""
# --- Precompute all answers ---
keypad = """123
456
789
x0x""".splitlines()

stk = [("1", 0, 0)] # start at "1" with r,c = 0,0 - state where we press button '1' once and have not moved
MOVES = [(1, 0), (0, 1)]
seen = set()
L_MAX = 4 # 3 might be enough - max len of string to append to stk

while stk:
    curr_s, r, c = stk.pop()
    n = int(curr_s)

    seen.add(n)
    
    if len(curr_s) > L_MAX:
        continue
    
    # Case 1 - repeatedly press most recent button
    # (we can repeatedly press the number so need to add to stk curr_s + curr_s[-1])
    press_again = curr_s + curr_s[-1]
    stk.append((press_again, r, c))
    
    # Cases 2-4 - move to and adj cell:
    # 2/ add the adjacent number on its own to start new strings - e.g. when reach 2 for the first time, must add 2 as a single new string so it can "start/head" its own series of strings (i.e numbs of the form "2....")
    # 3/ append the adjacent number to curr string - e.g. from 1 we reach 2 and 4 so this corresponds to adding state ("12",r=0,c=1) and ("14",r=1,c=0)
    # 4/ !! SKIP the adjacent number but continue from there with curr string - e.g. from 1 we reach 2 but DO NOT add '2' so state is ("1",r=0,c=1)
    #    e.g. consider 180; need to move from 1 to 2 but NOT ADD 2 etc.
    for dr, dc in MOVES:
        if (r_ := r + dr) < 4 and (c_ := c + dc) < 3:
            adj_number = keypad[r_][c_]
            if adj_number != 'x':
                stk.append((adj_number, r_, c_))
                stk.append((curr_s + adj_number, r_, c_))
                stk.append((curr_s, r_, c_))

# --- End of precompute step ---
T = int(input())

for _ in range(T):
    k = int(input())
    d = 0
    while True:
        if k + d in seen:
            print(k + d)
            break
        elif k - d in seen:
            print(k - d)
            break
        d += 1