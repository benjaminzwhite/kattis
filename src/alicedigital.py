# Alice in the Digital World
# https://open.kattis.com/problems/alicedigital
# TAGS: array, nice
# CP4: 3.5a, Max 1D/2D Range Sum
# NOTES:
"""
Nice exercise to get a linear solution.

I left meaningful variable names and comments below, logic should be clear.
"""
T = int(input())

for _ in range(T):
    n, m = map(int, input().split())

    xs = list(map(int, input().split()))
    xs.append(-1) # dummy element appended to end of array to trigger processing of last real element

    does_curr_contain_m = False
    curr_window_sum = 0
    curr_window_sum_after_m = 0

    best = 0

    for x in xs:
        if x < m:
            # process curr window and start new with 0 curr sum
            if does_curr_contain_m:
                best = max(best, curr_window_sum)
            curr_window_sum = 0
            curr_window_sum_after_m = 0
            does_curr_contain_m = False
        elif x == m:
            # process curr window and start new with curr_window_sum_after_m, reset this
            if does_curr_contain_m:
                best = max(best, curr_window_sum)
                curr_window_sum = curr_window_sum_after_m + x
                curr_window_sum_after_m = 0
            else:
                does_curr_contain_m = True
                curr_window_sum += x 
        else:
            curr_window_sum += x
            if does_curr_contain_m:
                curr_window_sum_after_m += x

    print(best)