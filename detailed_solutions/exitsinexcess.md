# Detailed solution for Kattis - Exits in Excess

[Problem statement on Kattis](https://open.kattis.com/problems/exitsinexcess)

This is a nice graph problem, it has a combinatorial feel a bit like an exercise in [Ramsey theory](https://en.wikipedia.org/wiki/Ramsey_theory) which is the inspiration I used when solving it in terms of coloring edges.

## Tags

graph, combinatorics, proof

## Solution

### Proof

Arrange the vertices in (without loss of generality) ascending order 1,2,3,4...

Draw all edges from lower to higher in **BLUE** (WLOG).

Now draw all edges from higher to lower in **RED**.

Observation: Any cycle, of any length, will involve a "backtrack" at some point i.e. **all cycles must contain BOTH some blue AND some red edges**.

By [pigeonhole principle](https://en.wikipedia.org/wiki/Pigeonhole_principle) applied to 2 sets containing a total of `m` edges: at least one of the `{BLUE, RED}` sets of edges will have `<= m/2` edges, so if you remove the smaller of the 2 sets you will be removing at most `m/2` edges, as required.

But when you do this you remove all edges of one color, and then by the converse of the Observation above **there cannot be any cycles remaining**.

### Implementation

So for each edge in the input, color it blue or red, and remove the family with fewest number of edges in it.

e.g. u,v: 1 to 7 will be colored blue since u < v

e.g. w,x: 5 to 4 will be colored red since  w > x

### Important note

Rereading the Output section, note that the Judge allows "suboptimal solutions".

For example, in Sample Input 3, the input data is **already cycle free** so don't need to remove any edges, and 0 is a valid answer.

But our solution approach will still suggest to remove the single red edge 3->2 even though it doesn't actually belong to a cycle.

(This is because the converse of the Observation is not true: All cycles must have edges of both blue and red colors in them, but a collection of edges of different colors does not necessarily create a cycle.

e.g. in Sample Input 3: 1->2, 1->3 are blue, 3->2 is red, but {1,2,3} is not a cycle)

## AC code

```python
_, m = input().split()

blue, red = [], []

for i in range(1, int(m)+1):
    u, v = map(int, input().split())
    if u < v:
        blue.append(i)
    else:
        red.append(i)

res = min((blue, red), key=len)

print(len(res))
for i in res:
    print(i)
```