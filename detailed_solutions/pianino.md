# Detailed solution for Kattis - Pianino

[Problem statement on Kattis](https://open.kattis.com/problems/pianino)

A nice array exercise, with some interesting edge cases during the implementation of the solution.

## Tags

array

## Solution

Basically for each value, count how many "ups" and "downs" have accumulated (i.e. take the net total: `-3 +5 = +2` ups, etc.) when you are at that value.

For example:

- If current value is 10 and first value, `fst`, was `4`, and there are net/acc `+2` ups to get to value `10`, then clearly the only `K` that would have scored arriving at this configuration would be `K = 3`, because `10-4 / 2` "ups" `= 6/2 = 3`. In other words, only a `K` of `+3` would land on `10`, starting from `4`, with a net `+2` "up moves".

So just do this for each value, but CARE! there is an important detail: you need to check that the delta (i.e. `10 - 4 = 6` in example above) is **evenly divisible by the net/accumulated amount** `+2` etc. (so for example, `7 // 2` is not allowed).

Another "edge case"/general observation:

Whenever you reach `0` with the net/acc up/down count:

- **any/all values of `K` would score `+1` at this point, and also...**
- ... the value `K = 0` would score here also

e.g. for `xs = 11 777 11`, arriving at `11` the second time, the net/acc up downs is `+1 -1 = 0`. So `K=3, 274, 13101...` etc. would all score +1 hit here, and also `K=0` would score here.

So track this, i.e. each time net/acc up down reaches `0`: increment by `1` a "global" counter for `ALL_KS`

The final result therefore is the `K` such that `d[K]` is max, but to this value you must add:

- `+1` **because the first value, `fst`, is always equal to the melody first value** (by construction, you get this one for free, so resuly is always >= 1 therefore)
- plus the `ALL_KS` score (to account for the net/acc hitting `0` some number of times)

### Implementation notes

I got a WA on first submit - I tested a few different inputs and found I had an implementation bug (in other words, the exercise is well designed and has good tests!):

When iterating over the final result dict, I was taking `v > max_v` and updating accordingly, and handing the `k=0` case separately. This leads to a situation where, if the `d[k=0]` result is say `95`, and the `d[123]` result is `90` but the `ALL_KS` additional value is `60` then I would produce result `k=0, v=95` (due to only considering `max_v`) when the real result is the `k=123, v=90+60`, since I was accounting for the `ALL_KS` extra flat amount **after** the `max_v` iteration, and since `95 > 90`, I was not getting to include the `+60` that puts the advantage for `k=123` overall.

So I slightly redesigned my code, I handle the `d[0]` by initializing `max_k, max_v = 0`. Then iterate over the `d{}` looking for `v > max_v` as before. However, now if `d[k=0]` produces the max value, since it is **not** in the dict, it will produce the final result `1 + max_v + ALL_KS = 1 + ALL_KS`, i.e. it matches the needed behavior for inputs like `xs = 8 8 8 8 8` where the optimal `k` value is `0`.

I left the initial bug in the code below for clarity.


## AC code

```python
N = int(input())

xs = list(map(int, input().split()))

d = {}
fst = xs[0]
acc_up_down = 0
ALL_KS_DUE_TO_acc_up_down_hit_zero = 0 # variable named to match the variable described in notes above O_o

for l, r in zip(xs, xs[1:]):
    if r < l:
        acc_up_down -= 1
    if r > l:
        acc_up_down += 1

    # which value of K, if any, would score here?
    if acc_up_down == 0:
        if r == fst:
            ALL_KS_DUE_TO_acc_up_down_hit_zero += 1
            #d[0] = 1 + d.get(0, 0) SEE UPDATES: this leads to weird max_v calculations/subtle error
    else:
        # if the AMOUNT difference between curr r and fst value in xs is delta = r - fst, and we are at "+2" up moves relative to start
        # then the only K value that would score here, if any, is delta//2 [and only if this division can be done in integers with no remainder]
        q, rem = divmod(r - fst, acc_up_down)
        if rem == 0:
            d[q] = 1 + d.get(q, 0)

# SEE UPDATE: this is where you have to be careful if you track d[k=0] separately - simpler to just treat 0 as the default k value
# and then, if no other k beats 0, final result will be 1 + 0 + ALL_KS so handled nicely.
max_k, max_v = 0, 0
for k, v in d.items():
    if v > max_v:
        max_k = k
        max_v = v

print(1 + max_v + ALL_KS_DUE_TO_acc_up_down_hit_zero)
print(max_k)
```