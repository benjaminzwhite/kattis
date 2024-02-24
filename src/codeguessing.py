# Code Guessing
# https://open.kattis.com/problems/codeguessing
# TAGS: logic, proof
# CP4: 3.2b, Iterative (Two Loops)
# NOTES:
"""
Nice little puzzle/exercise.

Listing all 6 combinations systematically avoids missing any cases.

Only 6 = 4!/2!2! patterns of 2 A's 2 B's:

Generally speaking you want the pattern to constrain so that each B only has 1 possible index so either you are
book-ending 2 B's or forcing each B against either of the edges (in position 1 and 9)

AABB -- max(A) = 7 -- res = 8 9
BBAA -- min(A) = 3 -- res = 1 2
ABBA -- max(A) - min(A) = 3 -- res = min(A)+1, min(A)+2
BAAB -- min(A) = 2 and max(A) = 8 -- res = 1 9
BABA -- min(A) = 2 and max(A) = 4 -- res = 1 3
ABAB -- min(A) = 6 and max(A) = 8 -- res = 7 9
"""
xs = list(map(int, input().split()))

CONDITIONS = {"AABB": (max(xs) == 7, "8 9"),
              "BBAA": (min(xs) == 3, "1 2"),
              "ABBA": ((max(xs) - min(xs)) == 3, f"{min(xs) + 1} {min(xs) + 2}"),
              "BAAB": (min(xs) == 2 and max(xs) == 8, "1 9"),
              "BABA": (min(xs) == 2 and max(xs) == 4, "1 3"),
              "ABAB": (min(xs) == 6 and max(xs) == 8, "7 9")}

s = input()

if CONDITIONS[s][0]:
    print(CONDITIONS[s][1])
else:
    print(-1)