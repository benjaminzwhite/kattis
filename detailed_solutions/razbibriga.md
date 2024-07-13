# Detailed solution for Kattis - Razbibriga

[Problem statement on Kattis](https://open.kattis.com/problems/razbibriga)

A nice combinatorics-based exercise, with some scope for improving algorithmic implementation also.

## Tags

mathematics, combinatorics, dict

## Solution

### Clarification of exercise statement

After not understanding the testcases and some time on the reading comprehension: it seems that the order is "fixed" - basically,  you are **not** allowed to freely flip words up/down etc. You must place the given words either left to right in the 2 rows, or top to bottom in the 2 columns, **as they are given**. This wasn't 100% clear to me from reading the statement (noe that this constraint reduces the combinatorics possibilities therefore).

### Main solution

Combinatorics: for all possible assignments of letters to the 4 corners: 

1. Fill the first "row or column" (whichever one of the 2 rows or 2 columns you want) in `d[start + end_letter]` ways i.e. using one of the words that starts and ends with the given row/columsn end points (**NOTE THIS MAY BE ZERO** in which case this configuration/assignment of letters to the 4 corners has 0 solutions)
2. Then fill second "row or column", third "row or column", fourth "row or column" same logic - in each case you have `d[this_row_or_column_start + end_letters]` ways of doing this

So final result is `product of all "num_ways for each row_or_column" for all 4 columns`

**However: note that you cannot reuse words** so you have to track, for each configuration, how many repetitions occur:

e.g. words `d = { AB:3, CV:1, BV:23153, ZZ:3 ..}`

and let's say current square assignment we are counting for is:

```
       A  B

       B  V 
```

- For row AB you can pick any of the `d[AB] = 3` words that start with A and end with B
- For column BV you can pick any of the `d[BV] = 23153` words that start with B and end with V
- However, for row BV, you can pick any of the `d[BV]` words that **HAVE NOT BEEN USED** so far, i.e. `23153 - 1 = 23152` words
- Similarly for column AB you can pick any of the `d[AB]` words that **HAVE NOT BEEN USED** so far, i.e. `3 - 1 = 2` words

**Note that this can cause some configs to be impossible due to not enough words:**

e.g. words `d = {FF:3, YX:201, BX:2...}`

and with curr square:
```
      F F
      F F
```

Starting with `tmp = 1` and chosing the rows or columns we get:

- chose row1 in `d[FF] = 3` ways, `tmp *= 3`, -->> `d[FF] -= 1`
- chose row2 in `"new d[FF]" = 2` ways, `tmp *= 2`  -->> `d[FF] -= 1`
- chose col1 in `"new d[FF]" = 1` ways, `tmp *= 1`  -->> `d[FF] -= 1`
- chose col2 in `"new d[FF]" = 0` **(NOTE THE 0 HERE!)** ways, `tmp *= 0`  -->> `d[FF] -= 1`

### Implementation note

Optimization: initially you could do something like `ALPHABET = abcde...xyz` but this will lead to taking product of the form `26*26*26*26`

If you realise though that you only need to use all the letters that actually appear as first or last element of a row or column, then you can just build the "effective ALPHABET" for the current testcase by adding them, as needed, from the testcase input instead of always initializing a full 26-char `ALPHABET`.


## AC code

```python
from itertools import product

#from string import ascii_uppercase as ALPH
ALPH = set() # optimization: only need to use all the letters that actually appear as fst,lst - might not need to take product of all 26*26*26*26

n = int(input())

d = {}
for _ in range(n):
    l = input()
    k = l[0] + l[-1]
    ALPH.add(l[0])
    ALPH.add(l[-1])
    d[k] = 1 + d.get(k, 0)

res = 0
for p in product(ALPH, repeat=4):
    N, E, S, W = p
    tmp = 1
    used = {}
    for fst, lst in [(N, E), (W, S), (N, W), (E, S)]:
        k_ = fst + lst
        tmp *= d.get(k_, 0) - used.get(k_, 0)
        used[k_] = 1 + used.get(k_, 0)
    res += tmp

print(res)
```