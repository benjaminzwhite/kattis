# Accounting aka Bokforing
# https://open.kattis.com/problems/bokforing
# TAGS: dict, logic, nice
# CP4: 2.3f, Hash Table (map), H
# NOTES:
"""
Really nice exercise; I wrote a detailed solution:

https://github.com/benjaminzwhite/kattis/blob/main/detailed_solutions/bokforing.md	
"""
N, Q = map(int, input().split())

d = {}
curr_generation = 0
recent_restart = 0 # question says everyone starts with 0 Kronor initially (such is life in Sweden O_o)

for _ in range(Q):
    op, *xs = input().split()
    if op == "SET":
        i, x = map(int, xs)
        d[i] = (curr_generation, x)
    elif op == "PRINT":
        i = int(xs[0])
        if i not in d:
            d[i] = (curr_generation, recent_restart)
        updated_generation, x = d[i]
        if updated_generation >= curr_generation: # TODO: can just be == curr_generation? since never can get ahead of it?
            print(x)
        else:
            print(recent_restart)
    elif op == "RESTART":
        recent_restart = int(xs[0])
        curr_generation += 1