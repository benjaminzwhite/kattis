# Limbo: Part 2
# https://open.kattis.com/problems/limbo2
# TAGS: logic, improve
# CP4: 5.2b, Finding Formula, Harder
# NOTES:
"""
TODO: IMPROVE: find a better solution

---

Quite experimental solution O_o just adjusted a few things as needed to match the pattern

General "idea" is += rows and cols up until you exceed the bottom_right corner value, that is always a power of 2
Then move back inwards, to reach the target R and target C, removing blocks_of_size_determined_by_current_r_and_c

Note: I found experimentally while trying to match results for 8x8 grid: final res depends on which direction you last moved in

Also, found it easier to use 1-based indexing
"""
T = int(input())
for _ in range(T):
    R, C = map(int, input().split())
    
    tar_R, tar_C = R + 1, C + 1 # found it easier to use 1-based indexing

    r, c = 1, 1
    direction = 1 # toggles whether we are doubling rightwards or downwards
    powers_of_two = 0

    while r < tar_R or c < tar_C:
        c *= max(1, 2 * direction)
        r *= max(1, 2 * (1 - direction))
        direction = (1 - direction)
        powers_of_two += 1

    if direction == 0:
        res = 2**powers_of_two - (c - tar_C) * r - (r - tar_R) - 1
    else:
        res = 2**powers_of_two - (r - tar_R) * c - (c - tar_C) - 1

    print(res)