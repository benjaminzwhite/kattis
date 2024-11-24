# Detailed solution for Kattis - ICPC Team Selection

[Problem statement on Kattis](https://open.kattis.com/problems/icpcteamselection)

A nice simple exercise where the "obvious" solution is suboptimal.

## Tags

logic, mathematics

## Solution

The "obvious" approach is to sort the values, and then to take the "middle value" of each group of 3. But if you design a few test cases, you'll see that this is actually suboptimal.

For example, consider the 9 values : `4 4 4 10 10 10 99 99 99` (here already sorted in ascending order).

If you take the sum of the 3 middle values (medians), you'll get `4 + 10 + 99` for a total of `113`.

However, if you try to "dilute the small values" into groups with larger medians, you'll find that you can do better: here for example, consider the following 3 groupings:

- `99, 99, 4`  median is `99`
- `99, 10, 4`  median is `10`
- `10, 10, 4`  median is `10`

Note how you the value `4` never occurs as a median now.

In general, the algorithm we are using here it to "pop largest value, twice" then "pop smallest value, once", to get each group of size 3.

In code, therefore, the occurence of the first median value is therefore at element `-2` in the list i.e. the penultimate element.

Then, move `-2` (**NOTE: -2, not -3!**) spots "backwards": do this `N` times `(-2*N)` but then adjust to `-2*N-1` for the fact that the end range index is **exclusive** (you need the `-1` to **include** the element at `-2*N`).

The above is much clearer if you just draw out a larger example with pen and paper and move through the elements to see which ones are getting added to your sum list. 


## AC code

```python
T = int(input())

for _ in range(T):
    N = int(input())
    xs = sorted(map(int, input().split()))
    res = sum(xs[-2:-2 * N - 1:-2]) # see comments above to understand this slicing behavior
    print(res)
```