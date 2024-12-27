# Detailed solution for Kattis - Stop Counting!

[Problem statement on Kattis](https://open.kattis.com/problems/stopcounting)

An interesting array-processing problem, like the classic range sum/"find media" exercises, but that I haven't seen before.

It's ranked quite highly, but there is a quite simple solution after reasoning a bit - maybe people are trying to find a dynamic programming or more complex approach?

## Tags

array

## Solution

Call the parts, "section 1", "valley", "section 2" - where valley may be empty.

Observation: for any choice of valley, if the average of the section 1 is higher than that of section 2, **it doesn't make sense to merge the 2 averages**, since this will lead to a lower total average.

Same argument for section 2 being higher than 1.

**So it never makes sense to "add" section 1 to section 2**; one or the other alone will be optimal.

So basically, you are looking for the **highest average value contiguous array**: note that since you must "start" with counting and "end" with counting,
you only need to consider contiguous arrays that either **start at `i=0`** or that **start at `i=len(arr)-1`**.

Note: this is why you can solve testcases with `N=1_000_000`; you don't have to consider e.g. `i=128` to `j=395` with `N**2` complexity, since such intermediate contiguous arrays would involve e.g. "stop counting" to `i=128`, "start counting", "stop counting" at `j=395` and this is **not allowed**.

## AC code

```python
N = int(input())
xs = list(map(int, input().split()))

best_sum = 0
best_cnt = 0

l_to_r_acc = 0
for curr_cnt, x in enumerate(xs, 1):
    # Implementation note: avoid floats by rewriting:
    # sum(curr_vals) / cnt(curr_vals) >= best_sum / best_cnt
    # as:
    # best_cnt * sum(curr_vals) >= best_sum * cnt(curr_vals)
    l_to_r_acc += x
    if (best_cnt * l_to_r_acc) >= (best_sum * curr_cnt):
        best_sum, best_cnt = l_to_r_acc, curr_cnt

r_to_l_acc = 0
for curr_cnt, x in enumerate(xs[::-1], 1):
    r_to_l_acc += x
    if (best_cnt * r_to_l_acc) >= (best_sum * curr_cnt):
        best_sum, best_cnt = r_to_l_acc, curr_cnt

if best_sum <= 0:
    print(0) # choose no cards option if all options lead to negative average
else:
    print(best_sum / best_cnt)
```
