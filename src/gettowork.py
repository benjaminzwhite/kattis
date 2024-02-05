# Get to Work
# https://open.kattis.com/problems/gettowork
# TAGS: sorting, greedy
# CP4: 3.4b, Involving Sorting, E
# NOTES:
"""
Greedy; just some input and output code also to handle.

Also 1 based indexing, so have dummy 0th element in res[] array
"""
from collections import defaultdict

C = int(input())

for case_num in range(1, C + 1):
    N, T = map(int, input().split())
    E = int(input())
    
    car_sizes = defaultdict(list)

    for _ in range(E):
        H, P = map(int, input().split())
        car_sizes[H].append(P)

    res = [0] * (N + 1) # INDEX 0 is dummy, so can use indexing as Town number 1,2,...

    IMPOSS = False

    for k, v in car_sizes.items():
        if k == T:
            continue # 0 cars needed to reach T since T is the target town (we are already there O_o)
        num_people_in_town = len(v)
        cars_needed = 0
        i = 0
        greedy = sorted(v, reverse=True)
        while i < len(greedy) and num_people_in_town > 0:
            num_people_in_town -= greedy[i]
            cars_needed += 1
            i += 1
        if num_people_in_town > 0: # people leftover who cannot get into any car from this town
            IMPOSS = True
            break
        else:
            res[k] = cars_needed

    if IMPOSS:
        print(f"Case #{case_num}: IMPOSSIBLE")
    else:
        print(f"Case #{case_num}:", *res[1:]) # res[1:] because 0 index of res is dummy, see above - 1 based indexing of employee IDs