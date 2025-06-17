# Jumping Yoshi
# https://open.kattis.com/problems/jumpingyoshi
# TAGS: graph, array, dfs, nice
# CP4: 8.2c, State-Space, BFS, H
# NOTES:
"""
I wrote a detailed solution:

https://github.com/benjaminzwhite/kattis/blob/main/detailed_solutions/jumpingyoshi.md
"""
from collections import defaultdict

N = int(input())
xs = list(map(int, input().split()))

as_source_scores = defaultdict(list)
as_target_scores = defaultdict(list)
for i, x in enumerate(xs):
    target_score = i - x
    source_score = i + x

    if target_score >= 0: # the min possible value of 'i + x' is when i == 0 and x == 0
        as_target_scores[target_score].append(i)
    
    if source_score <= N - 1: # the max posible value of 'j - y' is when j == N - 1 and y == 0 
        as_source_scores[source_score].append(i)


# CARE! see Implementation note - you always start at i=0, so res turns out to be the INDEX of furthest reached pebble.
stk = [0]
res = 0
seen = set()
while stk:
    curr_i = stk.pop()

    if curr_i in seen:
        continue
    seen.add(curr_i)
    
    res = max(res, curr_i)
    if res == N:
        # optimization, not sure if needed for AC: reached optimal result so break early from DFS
        break
    
    # find which vertices j have TARGET SCORE = i+x
    # try any edge from this SOURCE i to TARGET j:
    for j in as_target_scores[curr_i + xs[curr_i]]:
        stk.append(j)
    
    # find which vertices k have SOURCE SCORE == i-x
    # try any edge from OTHER SOURCES k to THIS TARGET i
    for k in as_source_scores[curr_i - xs[curr_i]]:
        stk.append(k)

print(res)