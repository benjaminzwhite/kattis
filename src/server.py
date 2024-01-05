# Server
# https://open.kattis.com/problems/server
# TAGS: basic
# CP4: 2.2l, List/Queue/Deque
# NOTES:
"""
If you want to use Python next() then can do something like this.
CARE! Make sure to use n as default argument for next() for cases where all the elements can be used:

from itertools import accumulate

res = next((i for i,x in enumerate(accumulate(tasks)) if x > T), n)

print(res)
"""
n, T = map(int, input().split())
tasks = map(int, input().split())
res = 0

for task in tasks:
    if task <= T:
        T -= task
        res += 1
    else:
        break

print(res)