# Detailed solution for Kattis - Jumping Yoshi

[Problem statement on Kattis](https://open.kattis.com/problems/jumpingyoshi)

This is one of my favorite exercises on Kattis so far; it's a really creative idea which involves finding a kind of "graph invariant", and realising that you can determine the edges in the graph in an efficient way despite the large `N` input size.

## Tags

graph, array, dfs

## Solution

The starting observation is that the pebbles form the vertices a graph of course, so we need to ask how/when are 2 pebbles connected in the "graph" given the input `xs` list?

Suppose you have 2 points `x, y` at index `i, j` respectively in the `xs` list:

```
   i = 0  1  2  3  4  5  6
  xs = 9  3  4  8  0  3  2
          ^              ^
          |              |
```

Say `i,x = (1,3)` and `j,y = (6,2)`. The condition for being able to travel from `i` to `j` is that the distance between the 2 pebbles (which is `j-i`) should equal the sum of the values `x+y`. **So an edge exists if `j-i == x+y`.**

In this particular example, therefore, you can indeed travel from `i=1` to `j=6` because: `i+x = 1+3 == 4` and we have `j-y = 6-2 == 4`.

**Here is the key insight:** if we rearrange the above simple equation so that each vertex's info is grouped on one side, we obtain the condition `i+x == j-y`, **and we note now that this is an entirely LOCAL/self-contained property of each individual vertex.** In other words, given the input `xs`, you can compute for each `i,x` its "score" `i+x` in a single pass through `xs`: you now know, for later, that `i,x` is connected to any other vertex which itself has a score `j-y` equal to `i+x`.

Note therefore that, each vertex effectively has **TWO** scores (if you prefer, flip role of `i` and `j` in the above):

- Call the value `i+x` the vertex `(i,x)`'s `source_score`
- Call the value `i-x` (i.e. `j-y`, we are just relabelling here) the vertex `(i,x)`'s `target_score`

So we are almost done - the remainder of the solution is as follows:

- Starting from the start vertex, you build the edges on a vertex by vertex basis
- You are trying to travel as far as you can, so you can use a standard DFS
- You can travel **to** all vertices which have a `target_score` equal to your current vertex's `source_score`
- You can also travel **from** all vertices which have a `source_score` equal to your current vertex's `target_score`

Note: I'm using "to" and "from" but that's a bit unclear - the graph isn't directed! I mean that in the above 2 cases, **to** means that current vertex plays the role of `i` and other vertices are playing the role of `j` and vice versa for **from**. It's just to emphasize that there are 2 different scores to consider whenever you reach a new vertex.


### Implementation notes

There is potential for off-by-one errors: The wanted result is the **maximum distance** you can travel. Since you start at `i=0` this works out to be the same as the index of the furthest pebble that you reach during the algorithm, e.g: if you start at the first pebble (which has index `i=0`) and can reach the pebble at index `3` then you are physically at the **4th pebble**, but you have travelled `3-0 = 3` distance in total.

## AC code

```python
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


# CARE! see Implementation note above - you always start at i=0, so res turns out to be the INDEX of furthest reached pebble.
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
```