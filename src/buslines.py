# Bus Lines
# https://open.kattis.com/problems/buslines
# TAGS: mathematics, graph, proof, nice
# CP4: 9.cons, Construction
# NOTES:
"""
Nice little exercise - see comments below about the 2 conditions.

The 'pairs' construction in the code below obviously builds all possible values exactly once:
- the first part builds all values from 1+2 to 1+n
- while the second part builds all values from 2+n to n-1+n

So you have all values, once, from 3 to 2*n-1 which is indeed the full range of (2*n-3) distinct sum values.
"""
n, m = map(int, input().split())

if m < n - 1:
    # cant form any tree
    print(-1)
elif m > 2 * n - 3:
    # max possible number of distinct values for endpoint sums e.g. vertices 1-8 can form 1+2=3,1+3=4...7+8 =15: there are 2*n-3 values
    print(-1)
else:
    pairs = [(1, snd) for snd in range(2, n + 1)] + [(fst, n) for fst in range(2, n)]
    for i in range(m):
        print(*pairs[i])