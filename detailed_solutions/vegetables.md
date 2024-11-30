# Detailed solution for Kattis - Boiling Vegetables

[Problem statement on Kattis](https://open.kattis.com/problems/vegetables)

An original problem involving a kind of "fair division" reasoning. I solved it in 2 different ways, shown below.

## Tags

logic, priority queue

## Solution

### First approach - logic and reasoning

Basically here's how to think about it:

- All vegetables with original weights are initially in one piece
- Your goal is to "reduce the difference between the maximum weight piece and the min weight piece" (think about it - that's a restatement of the problem; asking for "increasing the ratio of min_weight/max_weight above `>= T`")
- Now; **you can never INCREASE the `min_weight_piece` directly** since you can only cut pieces, but not join them
- So you can only improve the ratio by **decreasing the `max_weight_piece`**
- Now, the `max_weight_piece` results from a) An initial vegetable of weight `W`, b) the `current_number_of_pieces` that vegetable `W` has been divided into
- So basically, each step you want to find whichever vegetable is *currently* contributing the largest weight pieces; let's say it is vegetable `V` and has been cut into `6` pieces. You "undo" this division into `6` pieces and cut it into `6 + 1 = 7` pieces instead.

By "incrementing number of cuts by +1" each step you are doing a BFS and will find the minimum number of cuts required. Also, it's clear that this strategy is optimal due to the "maximum" property of the largest current piece.

#### Implementation comment

Array of `N` "num_pieces" which tracks the number of pieces that each of the `N` vegetables is currently divided into, initially all = 1

Then, on each step, find the index which has maximum `(vegetable weight / num_pieces)`, since this gives you the `max_weight_piece`

Then for that index, increment the `num_pieces[idx] += 1`; this models e.g. cutting a vegetable into "7" pieces now instead of "6"


## AC code

```python
T, N = input().split()
T = float(T)
N = int(N)

weights = list(map(int, input().split()))

num_pieces = [1] * N

min_weight_piece = 0
max_weight_piece = 1e9

cnt = 0 # remember to take -1 for result since will always cnt+1 with above initial conditions

# should avoid division here and compare ming_weight_piece < ( max_weight_piece * T ) instead 
while (min_weight_piece / max_weight_piece) < T:
    cnt += 1
    min_weight_piece = 1e9
    max_weight_piece = 0
    i_to_update = -1

    # find the vegetable whose current pieces are the heaviest, and add +1 cut to it
    # e.g if a veg is 9kg and is currently being cut into 3 pieces, while another is 5kg and cut into 1 piece
    # then IT IS THE LATTER THAT HAS current pieces = 5/1 = 5kg that contributes the MAX WEIGHT PIECE
    # while the former is contributing pieces of weight 9/3 = 3kg
    # So the algorithm will take 2nd vegetable and instead of cutting into 1 piece, will cut it into 1+1 = 2pieces.
    for i, (veg_weight, veg_pieces) in enumerate(zip(weights, num_pieces)):
        min_weight_piece = min(min_weight_piece, veg_weight / veg_pieces)
        if (veg_weight / veg_pieces) > max_weight_piece:
            i_to_update = i
            max_weight_piece = (veg_weight / veg_pieces)
    
    num_pieces[i_to_update] += 1
```

### Second approach - priority queue

(probably is faster? Maybe for huge inputs it's relevant, although I didn't time out with first approach)

- maintain 2 PQs `minheap`, `maxheap`
- `maxheap` tuple will be `(piece_weight, original_veg_weight, curr_num_pieces)`
- initialize with `(-x, x, 1)` for `x` in weights

Following logic from above 1st solution: at each step, we find the vegetable that is contributing the **maximum piece weigh** e.g. as before, if vegetable `V` of weight `60` has been cut into `3` pieces, its piece weight is `20`.

This value will be found with our `maxheap`; we pop that value, now we pretend that we take **that original vegetable and instead of e.g. `3` pieices it now has `3+1 = 4` pieces.**

`maxheap = [ (-20, 60, 3), .... ]` (CARE! note we have here `-20` due to Python `maxheap` behavior, need to take negative value)

We pop this tuple, and the knowledge of the values `60, 3` means that we know `-20` is from cutting piece `60` into `3` pieces so:

- we now cut `60` into `3+1 = 4` pieces, so we heappush: `(-15, 60, 4)` back to the `maxheap`
- we also heappush `15` to the **minheap** in case we have affected the minimum value also

**We perform this as long as the top value on the `minheap` and the top value on the `maxheap` are lower than the target ratio.**

## AC code

```python
from heapq import heappop, heappush

T, N = input().split()
T = float(T)
N = int(N)

weights = map(int, input().split())

minheap, maxheap = [], []

for w in weights:
    heappush(minheap, w)
    heappush(maxheap, (-w, w, 1)) # maxheap tuple will be (piece_weight, original_veg_weight, curr_num_pieces)

min_weight_piece, max_weight_piece = minheap[0], abs(maxheap[0][0]) # the minimum weight piece and max weight pieces are tracked by the min and maxheap respectively

cnt = 0
while (min_weight_piece / max_weight_piece) < T:
    cnt += 1
    
    curr_piece_weight, orig_veg_weight, curr_num_pieces = heappop(maxheap)
    new_piece_weight = (orig_veg_weight / (curr_num_pieces + 1)) # CUT INTO 1 MORE PIECE ie. go from e.g. 6 to 7 pieces
    
    heappush(minheap, new_piece_weight)
    heappush(maxheap, (-new_piece_weight, orig_veg_weight, curr_num_pieces + 1))
    
    min_weight_piece, max_weight_piece = minheap[0], abs(maxheap[0][0])

print(cnt)
```