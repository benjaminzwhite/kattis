# Detailed solution for Kattis - Accounting a.k.a. Bokforing

[Problem statement on Kattis](https://open.kattis.com/problems/bokforing)

This is a cool algorithmic idea, basically asking: how can you avoid updating all entries in a hash map ?

## Tags

algorithm

## Solution

The idea here is that you track "what is the current generation of update we are on" and the "most recent restart value that was used".

- track a global `curr_generation` counter that will `+= 1` each time there is a global reset.
- then when you process the queries, each time you make a `SET` query you track what generation the update was made in e.g. if person `abc` gets income `1400` in generation `2` their dict entry is set to `"abc" = (2, 1400)`.
- whenever there is a restart, you increase the current generation by +1.
- when you make a query there are 2 possibilities:
- A: if you find that the person being queried has their `generation >= curr_generation`, you know their info is up to date (i.e. since last restart).
- B: if you find their `generation < curr_generation`, then their data is **OUT OF DATE**, i.e. has NOT been updated since one (or more) of the recent restarts. So their value should in reality be `whatever_the_most_recent_restart_value_was`.

So we will track most recent restart value globally also, and use that in cases when queries reach "out of date" users.

## AC code

```python
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
```