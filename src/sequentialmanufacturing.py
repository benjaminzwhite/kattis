# Sequential Manufacturing
# https://open.kattis.com/problems/sequentialmanufacturing
# TAGS: logic, proof, nice, detailed solution
# CP4: 5.2a, Finding Formula, Easier
# NOTES:
"""
Very nice exercise: I wrote detailed solution:

https://github.com/benjaminzwhite/kattis/blob/main/detailed_solutions/sequentialmanufacturing.md
"""
N, P = map(int, input().split())
ts = list(map(int, input().split()))
ks = map(int, input().split()) # unused O_o

#     v-- first object goes through unencumbered in time sum(ts)
res = 1 * sum(ts) + (P-1) * max(ts)
#                     ^___ remaining P-1 objects are each sent with a delay of max_machine_time after the first one
print(res)