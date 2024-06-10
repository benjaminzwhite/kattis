# Name That Permutation
# https://open.kattis.com/problems/namethatpermutation
# TAGS: mathematics, combinatorics
# CP4: 5.3g, Factorial
# NOTES:
"""
Basically; find the kth permutation in lexicographic order - I've solved this elsewhere on other OJs
"""
from math import factorial

# used to use try/except for exercises when didn't know how many lines there were in test case O_o not very good practice
while True:
    try:
        n, k = map(int, input().split())

        xs = list(range(1, n + 1))

        res = []
        for delta in range(n):
            f = factorial(n - delta - 1)
            i = k // f
            res.append(xs[i])
            del xs[i] # delete this "character" as it has found its place in the permutation (here the "characters" are numbers from 1 to n where n might be 50 or whatever, but think of them as single characters like A,B,C... clearer imho)
            k %= f

        print(*res)
    except EOFError:
        break