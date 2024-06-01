# Generalized Recursive Functions
# https://open.kattis.com/problems/generalizedrecursivefunctions
# TAGS: dynamic programming, improve
# CP4: 2.2i, Big Integer
# NOTES:
"""
TODO: IMPROVE: My solution is 0.8 secs but there are faster Python ones - get faster solution

Left recursive version here below in notes also (is slower than using dp array, due to Python function calls I guess?)

---

from functools import lru_cache

T = int(input())
for _ in range(T):
    *AB, c, d = map(int, input().split())

    A = AB[::2]
    B = AB[1::2]

    @lru_cache(maxsize=None) # <-- note: times out if you remove maxsize=None O_o
    def f(x, y):
        if x > 0 and y > 0:
            return c + sum(f(x - a, y - b) for a, b in zip(A, B))
        else:
            return d

    XY = list(map(int, input().split()))
    X = XY[::2]
    Y = XY[1::2]

    for x, y in zip(X, Y):
        print(f(x, y))

    print()
"""
T = int(input())
for _ in range(T):
    *AB, c, d = map(int, input().split())

    dp = [[0] * 100 for _ in range(100)]

    for x in range(100):
        for y in range(100):
            if x > 0 and y > 0:
                dp[x][y] = c + sum(dp[max(0, x - a)][max(0, y - b)] for a, b in zip(AB[::2], AB[1::2])) # max(0,x-a) means that e.g. if x-a is negative we get dp[x=0] so will have been set to d already
            else:
                dp[x][y] = d

    XY = list(map(int, input().split()))

    for x, y in zip(XY[::2], XY[1::2]):
        print(dp[x][y])

    print()