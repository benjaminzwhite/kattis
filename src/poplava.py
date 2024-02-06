# Poplava
# https://open.kattis.com/problems/poplava
# TAGS: greedy, logic, proof, nice
# CP4: 9.cons, Construction
# NOTES:
"""
Nice problem.

The obvious approach works - try forming a basin bookended by the 2 largest values n and n-1.
Remove uneeded values and prepend them in ascending order, so that they dont contain any water volume.

---

Proof (by induction) that this greedy approach works:

Suppose using e.g. 1 -> n-1 you can form any total 1 <= k <= n * (n-1) // 2

Then when you allow element n, and want to form any number k' <= (n+1) * n // 2: you first remove n from total k' to get a new target k'' = k' - n 

This new k'' is <= (n+1) * n // 2 - n, which (after rearranging) is equal to  (n-1) * n // 2 therefore k'' <= n * (n-1) // 2.

By induction can form any such k'' without using n i.e. using only 1 -> (n-1), so we are done.
"""
N, X = map(int, input().split())

if N <= 2 or X > (N - 1) * (N - 2) // 2:
    print(-1)
else:
    prepend = []
    basin = []

    for x in range(1, N - 1):
        if N - 1 - x <= X:
            basin.append(x)
            X -= N - 1 - x
        else:
            prepend.append(x)

    print(*prepend, N - 1, *basin, N)