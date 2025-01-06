# Dodecaphony
# https://open.kattis.com/problems/dodecaphony
# TAGS: mathematics, modulo
# CP4: 1.6f, Real Life, Medium
# NOTES:
"""
CARE! for the "Inversion" need to check "and fst == new[0]" because in description:
"With inversions, the first note doesn't change"
"""
LOOKUP = "C C# D D# E F F# G G# A A# B".split()

L = int(input())
orig = input().split()
new = input().split()

# transposition, n is SHIFTED *UP* so do %12 trick:
n = (LOOKUP.index(new[0]) - LOOKUP.index(orig[0]) + 12) % 12

if all((LOOKUP.index(new[i]) - LOOKUP.index(orig[i]) + 12) % 12 == n for i in range(L)):
    print("Transposition")
elif orig == new[::-1]:
    print("Retrograde")
else:
    fst = orig[0]
    fst_idx = LOOKUP.index(fst)

    if all((LOOKUP.index(new[i]) - fst_idx + 12) % 12 == (fst_idx - LOOKUP.index(orig[i]) + 12) % 12 for i in range(1, L)) and fst == new[0]:
        print("Inversion")
    else:
        print("Nonsense")