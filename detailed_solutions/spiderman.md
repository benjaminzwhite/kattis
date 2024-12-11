# Detailed solution for Kattis - Spiderman's Workout

[Problem statement on Kattis](https://open.kattis.com/problems/spiderman)

This is a standard dynamic programming exercise, but it has the requirement of outputting the solution path and also one or two implementation details, so it's interesting to record comments here.

## Tags

dynamic programming

## Solution

I explain the dynamic programming states and transitions in the code below, it's clearer line by line.

One implementation comment though: I had a subtle bug for a while, it was in the lookbehind step - I was **always** updating the dp cell as follows:

`dp[row_index][curr_height] = (curr_distance, min(max_height, tmp_height))`

when the correct answer **checks first**, then updates:

```
if max_height < tmp_height:       
    dp[row_index][curr_height] = (curr_distance, max_height)
```

Note the slight difference - the updating needs to know that `max_height < tmp_height`  and only updates if so, rather than always updating.

## AC code

```python
T = int(input())

for _ in range(T):
    M = int(input())
    distances = list(map(int, input().split()))

    max_possible_height = sum(distances)
    IMPOSSIBLE = None

    # used to print rows during debugging
    DEBUG = False

    dp = [[IMPOSSIBLE] * (max_possible_height + 1) for _ in range(M)]

    # initialize dp board with first distance, which must be in +ve direction
    # UPDATE - ALSO TRACKING THE MAX HEIGHT REACHED IN THIS PATH - so RECORD A TUPLE (+/- the distance to reach this state, HIGHEST_HEIGHT_REACHED_SO_FAR)
    dp[0][distances[0]] = (distances[0], distances[0])

    # process the remaining distances in rows - call them curr_distance
    # for each of the possible height values (columns):
    # 1) look ahead from curr_height by + curr_distance and see if in PREVIOUS ROW, dp[prev][curr_height + curr_distance] has been set
    # if so, then we can climb DOWN from that height to this curr_height, since the delta is curr_height.
    # -- IMPLEMENTATION: instead of record True False, we can record the HEIGHT USED TO GET THERE (will be helpful for reconstruction)
    # 2) look behind from curr_height, see if in prev row dp[prev_row][curr_height - curr_distance] has been set
    # if so then we can climb UP *FROM* that height *TO* this curr height

    for row_index, curr_distance in enumerate(distances[1:], 1):
        for curr_height in range(max_possible_height):
            # lookahead
            if curr_height + curr_distance <= max_possible_height:
                if dp[row_index - 1][curr_height + curr_distance] is not IMPOSSIBLE:
                    #max_height reached by the above element is:
                    max_height = dp[row_index - 1][curr_height + curr_distance][1]
                    dp[row_index][curr_height] = (-curr_distance, max(max_height, curr_height + curr_distance)) # TRACK NEGATIVE AS DOWN MOVE
            
            # lookbehind -- CARE; curr_height must be >= curr_distance (dont flip the 2 in the comparison)
            if curr_height - curr_distance >= 0:
                if dp[row_index - 1][curr_height - curr_distance] is not IMPOSSIBLE:
                    #max height reached
                    max_height = dp[row_index - 1][curr_height - curr_distance][1]
                    # we could also be setting a NEW MAX HEIGHT if curr_height > max_height
                    max_height = max(max_height, curr_height)
                    #has the current dp cell been set?
                    if dp[row_index][curr_height] is not IMPOSSIBLE:
                        tmp_height = dp[row_index][curr_height][1]
                    else:
                        tmp_height = 1e9
                    if max_height < tmp_height:
                        dp[row_index][curr_height] = (curr_distance, max_height) # TRACK POSITIVE AS UP MOVE

    if DEBUG:
        for row in dp:
            print(row)

    # Our result state is described by last row of dp and first column (height 0)
    # If it is IMPOSSIBLE i.e. None, then there is no solution
    res = dp[-1][0]

    if res is IMPOSSIBLE:
        print("IMPOSSIBLE")
    else:
        # reconstruct solution
        sol = []
        curr_solution_tuple_idx = 0
        for dp_row in range(M - 1, -1, -1): # M is number of steps so M-1 is LAST ROW OF DP MATRIX, we work -1 UP EACH ROW UNTIL ROW 0
            delta = dp[dp_row][curr_solution_tuple_idx][0]
            if delta < 0:
                # we moved DOWN to reach this state
                sol.append('D')
            else:
                sol.append('U')
            # get next tuple
            curr_solution_tuple_idx = curr_solution_tuple_idx - delta
        print(''.join(sol[::-1])) # REVERSE SOL TO GET ORIGINAL ORDER
```