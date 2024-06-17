# Detailed solution for Kattis - The Sound of Silence

[Problem statement on Kattis](https://open.kattis.com/problems/sound)

A nice exercise for finding an efficient solution using sliding windows.

## Tags

sliding windows, deque

## Solution

We use several `deque` i.e. double ended queues where we can pop the leftmost element efficiently.

Without loss of generality, let's focus on the "big" elements i.e. the maxima in last `m` elements:

The key observation is: as soon as you encounter an element `x` that is bigger than previous "bigs", **then those previous bigs can't be maxima any more going forward.**

So: first, look at the head/first/leftmost elements of your deque of previous bigs, and keep checking that those elements have an *INDEX* that is within the current window size `m` (so, therefore, when you add elements to the deque you will also need to store their index in the input list).

You do this by checking that the *INDEX* of the tuple in the "bigs" deque is `<= i-m`, so that you know it belongs to current window.

Second, pop from "stack" all the maxima that are less than current `x` value:

- now you have a record of all maxima IN DESCENDING ORDER, and from oldest to newest index
- all of the elements in this current deque are within size `m` window; the largest *VALUE* is at the head (since you have "stack popped" until this is so)
- same reasoning for the "small"/minimum deque

Therefore the **first element of the big/small** contain, respectively, the biggest and smallest elements in current window of size `m`.

### Implementation notes

There is potential for off-by-one errors/indexing as always.

You need to check `if big[0][1] - small[0][1] <= c and i > m-1:` the **and** part is important, because you need `i > m-1` to ensure that have seen at least `m` elements so far.

You could just say `i >= m` to make it clear, since we are using `enumerate(xs, 1)` (1 based indexing so `i` is counting number of elements seen so far).


## AC code

```python
from collections import deque

n, m, c = map(int, input().split())
xs = map(int, input().split())

big = deque()
small = deque()

no_silence = True

for i, x in enumerate(xs, 1):
    while big and big[0][0] <= i - m:
        big.popleft()
    while big and big[-1][1] < x:
        big.pop()
    while small and small[0][0] <= i - m:
        small.popleft()
    while small and small[-1][1] > x:
        small.pop()

    big.append((i, x))
    small.append((i, x))

    if big[0][1] - small[0][1] <= c and i > m - 1: # m - 1 since using 1 based indexing in enumerate, i.e. i >= m
        print(i - m + 1)
        no_silence = False

if no_silence:
    print("NONE")
```