# Detailed solution for Kattis - Happy and Unhappy Numbers

[Problem statement on Kattis](https://open.kattis.com/problems/happyandunhappynumbers)

This is an interesting number theory/digit sequence property/combined with a range sum question: you need to work a bit to get a performant solution also.

I solved it in 2 ways, which are listed below in order of "cleverness" - the AC code for each solution is immediately below.

## Tags

mathematics, number theory, range sum

## Solution

### First approach

`N_MAX` is large for Python, maybe too much for other languages also (given the 7+ difficulty rating), and if you just "generate all happy numbers from 1 to `N_MAX`" it will time out.

However you can obtain a computational improvement by noticing that: **the permutation (of the digits) of any happy number is also happy and same for unhappy numbers.**

So, now, when generating using the `is_happy()` function, once you know that the **start value `x`** definitely leads to happy `{True, False}`, then you can update with:

- all the values in the `seen()` path to reach 1 (or those in the `seen()` cycle if `x` is **UNhappy**)
- **AND** update all permutations of **ALL** these values also

So basically then you can memoize using an array `H` by checking, for each subsequent `x`, whether `H[x] > -1` i.e. if it has already been encountered.

Then the "easy part" is that you form a precomputed `RES` which is a **range sum**, i.e. you accumulate `is_happy(x)` for `x=1` to `N_MAX` then can query range by taking `right index value - left index value` 

(Implementation note: remember to take **minus 1 index**, since you want range to be **INCLUSIVE**)


## AC code - first approach

```python
from itertools import permutations

N_MAX = 1_000_050
H = [-1] * N_MAX

def is_happy(x):
    if H[x] > -1:
        return H[x]

    seen = set()

    while True:
        if H[x] == 1 or x == 1:
            for y in seen:
                for p in permutations(str(y)):
                    tmp = int(''.join(p))
                    if tmp < N_MAX:
                        H[tmp] = 1
            H[x] = 1
            return 1
        elif H[x] == 0 or x in seen:
            for z in seen:
                for p in permutations(str(z)):
                    tmp = int(''.join(p))
                    if tmp < N_MAX:
                        H[tmp] = 0
            return 0
        seen.add(x)
        x = sum(d**2 for d in map(int, str(x)))

RES = [0] * N_MAX
for n in range(1, N_MAX):
    RES[n] = RES[n - 1] + is_happy(n)

T = int(input())
for _ in range(T):
    l, r = map(int, input().split())
    print(RES[r] - RES[l - 1]) # CARE! -1 due to taking INCLUSIVE range sum
```

### Second approach

Here is a cleverer way, after solving the first way and trying to improve performance/speed:

Note that, given a number with `NUM` digits, the maximum next value is `9 * 9 * NUM` since the max possible digit value is `9` and there are `NUM` of them.

So, given the exercise's stated maximum range `10**6`, **you only need to compute whether `x_1` is Happy/Unhappy for `x_1` in the range from `1` to `9 * 9 * 7`, where here the value `7` is because there are `NUM_DIGITS=7` digits in `10**6`**

Then for each `x`, you only need to check whether its first transformation (which will lead to a number in the above computed set of `x_1`'s) is happy/unhappy.

Then the rest of the code involving the precomputing and taking a range sum query is basically the same as first approach.


## AC code - second approach

```python
N_MAX = 1_000_050
NUM_DIGITS = 7 # max range is 10**6 so need to compute for 7 digits

CLEVER_HAPPY = set({1})
for x in range(1, 9 * 9 * NUM_DIGITS + 1):
    seen = set()
    while x not in seen:
        if x == 1:
            CLEVER_HAPPY.update(seen)
            break
        seen.add(x)
        x = sum(d * d for d in map(int, str(x)))


RES = [0] * N_MAX
for n in range(1, N_MAX):
    RES[n] = RES[n - 1] + (sum(d * d for d in map(int, str(n))) in CLEVER_HAPPY) # the sum() is checking whether n is_happy()

T = int(input())
for _ in range(T):
    l, r = map(int, input().split())
    print(RES[r] - RES[l - 1]) # CARE! -1 due to taking INCLUSIVE range sum
```