# Simple Factoring
# https://open.kattis.com/problems/simplefactoring
# TAGS: mathematics, basic
# CP4: 3.2h, Math Simulation, Easier
# NOTES:
N = int(input())

for _ in range(N):
    a, b, c = map(int, input().split())

    disc = b * b - 4 * a * c
    if disc >= 0: # CARE! >= rather than just >, else get WA
        r = int(disc**0.5)
        if r * r == disc:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")