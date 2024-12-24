# Detailed solution for Kattis - Kratki

[Problem statement on Kattis](https://open.kattis.com/problems/kratki)

This exercise is an application of combinatorics/Ramsey theory, and then requires you to actually implement a nice construction logic. It's also a performance exercise (at least in Python because the `N = 10**6` will cause TLE otherwise) so you have to generate the arrays/ranges efficiently (this might not be a problem in C++ so worse approaches might work there).

## Tags

mathematics, combinatorics, proof

## Solution

### Proof background

By the [Erdos-Szekeres theorem](https://en.wikipedia.org/wiki/Erd%C5%91s%E2%80%93Szekeres_theorem) on a sequence `N` distinct integers: if `N = m*n + 1` then the sequence must contain a monotonic increasing (resp. decreasing) subsequence of length `m+1` or a monotonic decreasing (resp. increasing) subsequence of length `n+1`.

If we want `K` to be the length of the largest monotonic subsequence then, you want the `max(m,n)` to be as small as possible, which requres `m`, `n` to be as close as possible i.e `m = n ~ sqrt(N)`

In any case, we need `K >= sqrt(N)` otherwise there will definitely be a monotonic subsequence of length greater than `K`, contradicting maximality of `K` requirement

### Construction

My first intuition was to go for some zigzag/interleaving behavior like `1 5 2 4 3` etc. but then it needs lots of adjustments, for ex. I was trying `N=7 k=3`, and getting `4 1 7 3 6 2 5` by swapping the "rises" and "falls" but it's super clunky.

Seeing the `sqrt(N)` made me think of geometric proofs like `. .. ... .... = 4*(4+1)//2` etc.
 
If you sort the N values and cut them up into a "square":

```
                 7 8 9  -> increasing len 3
                 4 5 6  -> 
                 1 2 3  ->
                 | | |
                 v v v decreasing len 3
```

and then rearrange/flatten: `7 8 9 / 4 5 6 / 1 2 3`, you see that the **increasing** subsequence are **within** the "chunks" while the **decreasing**
subsequences are **amongst/between** "chunks" - so the length of the `incrasing <=> SIZE` of chunks, length of the `decreasing <=> NUMBER` of chunks.

- When N is not a perfect square, works the same: e.g. `N=15, k=4 -> sqrt(N = 15)= 3.something` which is indeed `<= k=4`

```
N=14             11 12 13 14   -> 4 length corresponding to k=4
k=4               7  8  9 10   -> 4
                  3  4  5  6   -> 4
                  1  2           
```

Flatten: `11 12 13 14 / 7 8 9 10 / 3 4 5 6 / 1 2` - again, longest chunk length is `4`, number of chunks is `4`, so longest monotonic sequence is `4` across or downwards.

- Finally, generalizing for when you want larger `k` value ("different aspect ratio" of the above square starting point):

```
N=14          9 10 11 12 13 14             
k=6           3  4  5  6  7  8
              1  2
```

Flatten: `9 10 11 12 13 14 / 3 4 5 6 7 8 / 1 2` - longest chunk length is `6`, number of chunks is `3` so longest monotonic sequence is `6` as required.

### Implementation note and performance

While implementing the above approach, I noted that `N` is `10**6` so it's actually a performance exercise (in Python at least) if you do flatten and range stuff as described above (building multiple lists etc.), so just copying the implementation above will get TLE.

I reworked the **implementation** (same logic, but now just find some easy-to-print arrangement of the "square" row/column breakdown)

Found this approach which works well (code golf practice was useful after all!) - it's yet another different way of getting the same "mathematical" answer
i.e. chunks of size `k`, of which there are `ceil(N/K)`.

- Note: that the `min(N, (i+1)*K)` is there to handle the case of the last chunk e.g. here handles `14 13` instead of printing `18 17 16 15 14 13`

```
for i in range(N // K + 1):
    print(*range(min(N, (i + 1) * K), i * K, -1))
    print()

# this will print for N=14, k=6:
6 5 4 3 2 1 / 12 11 10 9 8 7 / 14 13
# note: here the / are just visually indicating the boundaries between the i'th and i+1'th chunks
```

## AC code

```python
from math import sqrt 

N, K = map(int, input().split())

if K < sqrt(N):
    print(-1)
else:
    res = []
    for i in range(N // K + 1):
        res.extend(range(min(N, (i + 1) * K), i * K, -1))
    print(*res)
```
