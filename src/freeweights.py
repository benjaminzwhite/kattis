# Free Weights
# https://open.kattis.com/problems/freeweights
# TAGS: binary search, improve
# CP4: 3.3b, Bisection and BSTA, E
# NOTES:
"""
TODO: IMPROVE: On first submit I couldn't get some edge cases to work properly, so left local comments
Also, therefore, there might be a simpler approach than what I have below
"""
n = int(input())

first_row = list(map(int, input().split()))
second_row = list(map(int, input().split()))

# ascending order, the weights that appear
# in binary search we guess MIDDLE INDEX <--- not the value, the index!!! 
WEIGHTS = sorted(set(first_row + second_row))
l, r = 0, len(WEIGHTS) - 1

lowest_we_need_to_lift = -float('inf')

while l <= r:
    mid = (l + r) // 2
    guess_w = WEIGHTS[mid]
    can_roll_all_heavier = True
    for row in [first_row, second_row]:
        curr_higher = -1 # NOTE THIS MUST BE RESET ON EACH OF THE 2 ROWS!!!!
        for x in row:
            if x >= guess_w:
                if curr_higher == -1:
                    curr_higher = x
                else:
                    if curr_higher != x:
                        can_roll_all_heavier = False
                        lowest_we_need_to_lift = max(lowest_we_need_to_lift, guess_w)
                        break
                    else:
                        curr_higher = -1 # reset, since this pair was OK
        
        if curr_higher != -1: # WE HAVE AN UNPAIRED ELEMENT IF WE END THE ROW WITH A CURR_HIGHER THAT HASN'T BEEN RESET
            can_roll_all_heavier = False
            lowest_we_need_to_lift = max(lowest_we_need_to_lift, guess_w)

    if can_roll_all_heavier:
        r = mid - 1 
    else:
        l = mid + 1

if lowest_we_need_to_lift != -float('inf'):
    print(lowest_we_need_to_lift)
else:
    print(0)