# Detailed solution for Kattis - Tram

[Problem statement on Kattis](https://open.kattis.com/problems/tram)

This isn't a very difficult exercise, but it's a nice revision of some geometry and has a clean answer in the end.

## Tags

mathematics, geometry

## Solution

The line is `y = x + a`, so `x - y + a = 0`.

The distance of an arbitrary point `X,Y` to a line defined by `p*x + q*y + r*a = 0` is: `| p*X + q*Y + r*a | / sqrt(p**2 + q**2)`

where, replacing coefficients, for us we have: `p*x + q*y + r*a = 0 ---> p = 1, q = -1, r = 1`

Thus distance is: `| X - Y + a | / sqrt(1**2 + 1**2)` and we note that this denominator simplifies to `sqrt(2)`.

Now, implementation detail: take **squared distances** instead of distances, and minimise sum of square distances (this makes the calculus easier).

```
f(a) = sum ( ( X - Y + a)**2 / 2 )

minimise with respect to a, and where the sum ranges over all (X,Y) in the dataset

df/da = sum(X - Y + a) => which we want to set to 0
```

Note here that you get `N` times `a` contributions to the sum, which you can take out of sum: `sum(X-Y) + sum(a + a + ...) = sum(X-Y) + N*a` which we want to set to `0`.

Thus after setting to `0` and rewriting, the condition becomes: `N*a = -sum(X-Y)`, or `N*a = +sum(Y-X)`

## AC code

```python
N = int(input())

res = 0
for _ in range(N):
    xi, yi = map(int, input().split())
    res += (yi - xi)

print(res / N)
```