# Paul Eigon
# https://open.kattis.com/problems/pauleigon
# TAGS: basic, logic
# CP4: 5.2a, Finding Formula, Easier
# NOTES:
N, P, Q = map(int, input().split())

if ((P + Q) // N) % 2 == 0:
    print("paul")
else:
    print("opponent")