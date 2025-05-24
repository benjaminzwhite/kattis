# Andrew the Ant
# https://open.kattis.com/problems/andrewant
# TAGS: logic
# CP4: 3.4d, Involving Sorting, H
# NOTES:
"""
I wrote a detailed solution:

https://github.com/benjaminzwhite/kattis/blob/main/detailed_solutions/andrewant.md
"""
while True:
    try:
        L, num_ants = map(int, input().split())
        
        ants = []
        acc_L, acc_R = 0, 0
        max_left_time, max_right_time = -1, -1
        for _ in range(num_ants):
            x, direction = input().split()
            x = int(x)

            if direction == 'L':
                acc_L += 1
                max_left_time = max(max_left_time, x) # ant travels leftwards from x to 0 so distance = x-0 = x
            else:
                acc_R += 1
                max_right_time = max(max_right_time, L-x) # ant travels rightwards from x to L so distance = L-x
            
            ants.append((x, direction))

        ants = sorted(ants)

        max_time = max(max_left_time, max_right_time)
        res = f"The last ant will fall down in {max_time} seconds - started at "
        
        # check the 3 cases
        if max_left_time > max_right_time:
            # find the acc_L'th ant -> in INDEX acc_L-1 in the sorted ants list:
            res += f"{ants[acc_L - 1][0]}."
        elif max_right_time > max_left_time:
            # find the -acc_R'th ant ==> same as acc_L+1th ant, which is in INDEX acc_L+1-1 = acc_L O_o
            res += f"{ants[acc_L + 1 - 1][0]}."
        else:
            # both the ants 'd' and 'e' abcd|efghij  fall off at same time
            res += f"{ants[acc_L - 1][0]} and {ants[acc_L + 1 - 1][0]}."

        print(res)

    except:
        break