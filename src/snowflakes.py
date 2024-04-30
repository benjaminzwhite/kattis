# Unique Snowflakes
# https://open.kattis.com/problems/snowflakes
# TAGS: dict, nice
# CP4: 2.3f, Hash Table (map), H
# NOTES:
"""
Nice little exercise; solution with variable names below should explain the logic O_o
"""
T = int(input())

for _ in range(T):
    n = int(input())
    xs = [input() for _ in range(n)]
    last_seen = {}
    rightmost_duplicate = 0
    curr_len = 0
    best = 0
    for i, x in enumerate(xs):
        if x not in last_seen or last_seen[x] < rightmost_duplicate:
            last_seen[x] = i
            curr_len += 1
            best = max(best, curr_len)
        else:
            best = max(best, curr_len)
            rightmost_duplicate = last_seen[x]
            last_seen[x] = i
            curr_len = i - rightmost_duplicate

    print(best)