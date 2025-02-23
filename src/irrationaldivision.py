# Irrational Division
# https://open.kattis.com/problems/irrationaldivision
# TAGS: logic, proof, nice
# CP4: 0, Not In List Yet
# NOTES:
"""
I wrote a detailed solution:

https://github.com/benjaminzwhite/kattis/blob/main/detailed_solutions/irrationaldivision.md
"""
p, q = map(int, input().split())

# Case 1: detailed in notes
# p is even
if p % 2 == 0:
    print(0)
else:
    # Case 2: detailed in notes
    # p is odd
    # Subcase: q is odd also:
    if q % 2 == 1:
        print(1)
    else:
        # Subcase: q is even:
        # Extra condition: can opponent, on their turn, cut their dimension DOWN to form an odd square to give back to you ?
        # If so, they can cancel your score
        if p > q:
            # e.g. p = 5, q = 4 -> opponent takes 1 col or 3 cols and leaves you seeing q-1 or q-3 * p rectangle:
            # e.g. WLOG 3*5 rectangle: you cut 2 of your "columns" and handover 3x3 oddsquare with white in topleft, which scores -1 for opponent
            print(0)
        else:
            print(2)