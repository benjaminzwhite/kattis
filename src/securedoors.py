# Secure Doors
# https://open.kattis.com/problems/securedoors
# TAGS: basic
# CP4: 2.3d, Hash Table (set)
# NOTES:
"""
Not a problem note, but found some weird Python behavior I didn't know about:

When making the res = f-string : for the formatting, you need to mix " and ' to get the " to appear O_o!?

Saw on StackOverflow that someone else had the same problem, and that it might change in Python 3.12
"""
N = int(input())

action = {"entry":"entered", "exit":"exited"}
seen = set()

for _ in range(N):
    op, x = input().split()
    res = f'{x} {action[op]}{" (ANOMALY)" if (op == "entry" and x in seen) or (op == "exit" and x not in seen) else ""}'
    print(res)
    if op == "entry":
        seen.add(x)
    else:
        seen.discard(x)