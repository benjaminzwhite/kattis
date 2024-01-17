# Forced Choice
# https://open.kattis.com/problems/forcedchoice
# TAGS: basic
# CP4: 1.4g, 1D Array, Easier
# NOTES:
N, P, S = map(int, input().split())

for _ in range(S):
    m, *xs = map(int, input().split())
    if P in xs:
        print("KEEP")
    else:
        print("REMOVE")