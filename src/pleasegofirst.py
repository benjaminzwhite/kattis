# Please, Go First
# https://open.kattis.com/problems/pleasegofirst
# TAGS: array, nice, detailed solution
# CP4: 5.2b, Finding Formula, Harder
# NOTES:
"""
I wrote detailed solution:

https://github.com/benjaminzwhite/kattis/blob/main/detailed_solutions/pleasegofirst.md
"""
T = int(input())

for _ in range(T):
    _ = input()
    s = input()

    d = {}

    for i,x in enumerate(s):
        # store HOW MANY PEOPLE ARE IN EACH GROUP, and SCORE i.e. RIGHTMOST INDEX for each group
        if x not in d:
            d[x] = (1, i)
        else:
            cnt, score = d[x]
            d[x] = (cnt + 1, i)

    seen = set()
    curr_longest_wait = len(s) - 1
    savings = 0

    for x in s[::-1]:
        if x in seen:
            continue
        seen.add(x)
        cnt, score = d[x]
        savings += cnt * (score - curr_longest_wait)
        curr_longest_wait -= cnt

    print(savings * 5) # you have to multiply the number of saved positions by 5 seconds for some reason