# Permuted Arithmetic Sequence
# https://open.kattis.com/problems/permutedarithmeticsequence
# TAGS: mathematics, sorting
# CP4: 5.2e, Number Systems/Seqs
# NOTES:
T = int(input())

for _ in range(T):
    _, *xs = map(int, input().split())
    delta = xs[1] - xs[0]
    if all(r - l == delta for l, r in zip(xs, xs[1:])):
        print("arithmetic")
    else:
        xs = sorted(xs)
        delta2 = xs[1] - xs[0]
        if all(r - l == delta2 for l, r in zip(xs, xs[1:])):
            print("permuted arithmetic")
        else:
            print("non-arithmetic")