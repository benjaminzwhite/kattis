# Watch Out For Those Hailstones!
# https://open.kattis.com/problems/hailstone
# TAGS: mathematics, basic, recursion
# CP4: 5.2e, Number Systems/Seqs
# NOTES:
def h(n):
    if n == 1:
        return 1
    else:
        if n % 2 == 0:
            return n + h(n // 2)
        else:
            return n + h(3 * n + 1)

N = int(input())

print(h(N))