# Detailed solution for Kattis - Digit Division

[Problem statement on Kattis](https://open.kattis.com/problems/digitdivision)

This is a good divisibility-related mathematics exercise; I found my solution by using a kind of [stars and bars](https://en.wikipedia.org/wiki/Stars_and_bars_(combinatorics)) breakdown/separation of the digit string, as explained below.

## Tags

mathematics

## Solution

Think about where you can insert a separator, `|`, in the digit string:

e.g. with the first testcase, with number `1246` and divisor `2`, we start with `|1246` and on each step we are looking at the number formed to the left of the current separator position:

`1|246` - 1 not divisible by 2
`12|46` - 12, divisible by 2, OK can place separator here
`124|6` - 124, divisible by 2, OK can place separator here
`1246|` - 1246, divisible by 2, OK can place separator here

If you now consider the general end result, with multiple separators, `|`, in a given digit string you note that for any large prefix, i.e. sequence terminated by a separator, you can consider what happens when you remove any separator within that prefix: **You will find that all subsequences formed will be divisible by `d` !**

For example, suppose we have as large prefix `12|4|98|36|` and we have `d=2`. Consider breaking this prefix into `124|` and `98|36|`: since `124` is `k * d` for some `k`, and  `1249836` is `l * d` for some `l`, then `9836 = (l * d) - (k * d * 10**some_exponent)` is also `something * d` so it is divisible by `d`.

So the answer is that "you can toggle on/off any of the separators `|` and form a valid subsequence" therefore the answer is `2 ** number of toggle-able separators`.

### Implementation note

**Important:** one subtle point (to avoid off-by-one error) is that you need to count the number of toggle-able separators correctly:

In the above examples, you need to **NOT** count the final `|` since the latter is not actually "toggle-able".

e.g. with `749` and `d=7` then you have `7|49`, not actually `7|49|` as toggles, otherwise you are double counting `7 49|` and `7 49`.

e.g. with `12|4|6|` the only toggleable ones are actually `12|4|6`  otherwise you double count `12|46|` and `12|46`.

In other words the answer is `2 ** (cnt of separators - 1)` since `cnt of separators - 1` is the actual number of toggleable separators.

**Important:** you also need to ensure that the entire input number itself is divisible by the `d`. Otherwise this approach fails on inputs like e.g. `s = 888881` with `d=2`, because even though I count 5 valid prefixes, the end/rightmost is not divisible by `d=2`.

So you need an extra check: you want `s` itself to be divisible by `d`. Clever implementation: converting huge `s` to int is not clever; so you can just check if the final `prefix % d` that you calculated already is itself divisible by `d` (see code below).


## AC code

```python
BIGMOD = 10**9 + 7

_, d = map(int, input().split())
s = input()

cnt = 0
prefix = 0
for c in map(int, s):
    prefix = prefix * 10 + c # to avoid recounting divisibilty, just *= 10 and shift digits leftwards each iteration
    prefix %= d # avoid TLE due to huge numbers: take the % of prefix each step to keep value small
    if prefix == 0:
        cnt += 1

# These are the extra checks described in the Implementation notes above
# Without these, you will get WA on some testcases - consider for example something like s=888881 with d=2
if prefix % d == 0 and cnt > 0:
    res = pow(2, cnt-1, BIGMOD)
else:
    res = 0

print(res)
```