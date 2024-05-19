# Detailed solution for Kattis - Powers and Modulus

[Problem statement on Kattis](https://open.kattis.com/problems/powers)

Practice for number theory reasoning and telescoping combinatorial identities.

## Tags

mathematics, number theory

## Solution

We have `S` given as:

`S = 1**b + 2**b + 3**b + ... + (a-1)**b + a**b`

In general `(a - n)**b` is, by binomial theorem, equal to `a**b + comb(b,1)*a**(b-1)*(-n)**1...`

i.e. a polynomial in `a` which will therefore have all its terms in `a` vanish `mod a` except the `comb(b,b)*a**(0)*(-n)**b` constant term.

So in the expression `S`, you can consider the "opposite" pairs: `1**b + (a-1)**b`, `2**b + (a-2)**b` etc. and since the right-hand side will only contribute `(-1)**b`, `(-2)**b` etc. when taken `mod a`, **and since we are told that `b` is odd**, then **all these pairs sum to `0` since they are of the form**: `1**b + (-1)**b` with `b` odd i.e. will be `1 - 1 = 0`.

The unpaired terms are:

- `a**b`, which is equal to 0 `mod a`
- and if `a` is **EVEN** you have a term `(a//2)**b` 

e.g. if `a = 8`, you pair off `1-7`, `2-6`, `3-5`, you take `8**b == 0 mod 8`, and you are left with the term `8//2 = 4**b`

But if `a` is **ODD** you don't get **any** unpaired terms, so then the sum is `0 mod a`

Summary: so the answer is `(a // 2)**b % a` if `a` is even else `0`.


## AC code

```python
a, b = map(int, input().split())

res = pow(a // 2, b, a) if a % 2 == 0 else 0

print(res)
```