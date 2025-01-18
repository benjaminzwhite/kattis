# Detailed solution for Kattis - ETA

[Problem statement on Kattis](https://open.kattis.com/problems/eta)

This is one of my favourite exercises on Kattis so far, it's really clever. It's a good example of how "changing representation" helps sometimes solve exercises - here from a "graph" to a "histogram" of the `d`'s, as explained in solution below.

## Tags

mathematics, graph

## Solution

Instead of thinking about "max degrees/distances etc." the better start point is **a star graph**.

The key observation is: if you want to have a vertex at a distance of `d=7` **you must have at least one vertex at** `d=6,5,...` etc.

So consider a **histogram of the distances** bins (forget `a,b` for now, just suppose you have a graph with `v` vertices) - an **original star graph configuration will look like this**:

```
            .
            .
            .
            .
          . .
        d=0 1 2 3 4 5   HERE V=6 vertices .  and 1 is in d=0, V-1 = 5 are in d=1 initially. d_max is 5
```

You always have 1 vertex in `d=0`, and let all other `V-1` be in `d=1`.

- **This initial configuration produces expectation =** `(1*0 + V-1 * 1 ) / V = (V-1) / V`

This is where I had insight: I was trying to explicitly "pair off" `d=1`'s into smaller amount of `d=2`'s etc, but notice that when you obtain any different configuration, the **new expectation will increase by `1/v` times the number of "`.` shifts" in total !!**

For example if the new graph configuration has `1 d=0`, `4 d=1`, and `1 d=2`, you shift a `.` from `d=1` to `d=2`, this decreases expectation by `1 * d=1/v` and increases it by `1 * (d=1+1=2)/v` , for a net delta of `1/v` !

If you shift e.g. a cube from `d=3` to `d=7` you get `+4/V` to expectation, etc.

**So now just need to think about the constraints on `.` shifting around:**

```
            . _
            .  |
            .  |--- there are V-2 MOVABLE/SHIFTABLE . IN THE d=1 bin
            . _|
          . .
        d=0 1 2 3 4 5 
```

You can only move `V-2` of the `.` in the `d=1` bin, because as discussed before, you must have at least **one** `d=1` `.` leftover if you have any `d=2,d=3...` etc.

- Similarly, if you were to move all `V-2` of these `d=1` bins to `d=2`, you can only then move `V-2-1=V-3` of the `d=2` bins to `d=3`, since you need at least 1 leftover `d=2` bin

So by Gauss schoolboy summation trick, the `max_number` of shifts you can perform, for a star graph with `V` vertices, is `(V-2) * (V-1) // 2`.

So, for a given `a,b` the goal is to find a sufficiently large number of "blocks" to get a "high enough resolution" such that you can move sufficiently many `.` each increasing expectation by `1/v`, to reach the given `a/b` endpoint.

**Note therefore that this means that `v` must be divisible by the original `b` in any case.**

So introduce 2 variables `a_prime` and `b_prime` such that `a' = s*a, b' = s*b` (thus `a'/b' = a/b`)

The initial star graph therefore has expectation `(b' - 1) / b'`, and you want to reach `a' / b'`, so you need how many shifts of `1/b'` each?: you need `a' - b' + 1` shifts, each of `1/b'`

As discussed, we know that for given `V` you can produce max_number of shifts = `(V-2) * (V-1) // 2` where `V = b'` is the number of vertices in our final graph, so we must have, combining with the result just above: `a' - b' + 1 <= (b' - 2) * (b' - 1) // 2`.

### Summary and implementation notes

1) Find the `a'` and `b'` for the given input `a,b`
2) Now perform the `a' - b' + 1 = num_shifts_needed` shifts
3) do 2) by initializing a distances array = `[1, b'-1, 0,0,0,0,0]` (corresponding to original star graph config)
4) for each step in 3), you try shifting as many at `curr_distance (d=1,2,3...)` as possible to next largest distance. You can only shift `x-1` at most where `x = distances[d]`, since you **must leave `1` behind if you perform at least `1` shift to `d+1`**
5) while doing 5), track the `num_shifts_needed` -> decrement each step until you reach 0 shifts needed

**Finally output step:**

You end up with a distances array encoding the final shifted graph transformed from star graph: it's just a bit tricky but just translate this info into **connectivity/vertex labelling info.**

e.g. for `a,b = 7,4` testcase I get distances = `[1, 1, 5, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]`

This means you have:

- one vertex at `d=0` to the target -> label it V=1
- one vertex at `d=1` to the target -> label it V=2, it is connected to V=1
- five vertices at `d=2` to the target **i.e. at distance 1** to `d=1` vertices -> **use the `last_used_d=1` vertex as the "canonical one" and connect all to it**: V=2 connected to V=3,4,5,6,7
- one vertex at `d=3` to target -> again, use `last_used_d=2` vertex as canonical one, and connect this vertex V=8 to it -> V=8 connected to V=7 

## AC code

```python
flg = True
a, b = map(int, input().split('/'))
if a < b - 1:
    flg = False

a_prime, b_prime = a, b

# you can solve this analytically if you want, I'm just keeping the logic from the notes above for clarity
while a_prime - b_prime + 1 > (b_prime - 2) * (b_prime - 1) // 2:
    a_prime += a
    b_prime += b

num_shifts_needed = a_prime - b_prime + 1

distances = [0] * (b_prime + 10) # +10 is just a sentinel value
distances[0] = 1
distances[1] = b_prime - 1 # originally all in d=1 

curr_d = 1
while num_shifts_needed > 0:
    max_can_shift = distances[curr_d] - 1 # must leave 1 behind
    if max_can_shift >= num_shifts_needed:
        distances[curr_d] -= num_shifts_needed
        distances[curr_d + 1] += num_shifts_needed
        num_shifts_needed = 0
    else:
        distances[curr_d] = 1
        distances[curr_d + 1] = max_can_shift
        num_shifts_needed -= max_can_shift
    curr_d += 1

# printing, see implementation notes
if not flg:
    print("impossible")
else:
    # Always produces a tree on b_prime vertices and b_prime-1 edges therefore:
    print(b_prime, b_prime - 1)
    curr_vertex_label = 2
    for d, cnt in enumerate(distances[1:curr_d + 5], 1): # +5 is sentinel
        for v in range(curr_vertex_label, curr_vertex_label + cnt):
            print(curr_vertex_label - 1, v)
        curr_vertex_label += cnt
```
