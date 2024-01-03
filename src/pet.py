# Pet
# https://open.kattis.com/problems/pet
# TAGS: basic
# CP4: 3.2b, Iterative (Two Loops)
# NOTES:
"""
- assigning input() not needed, first days using Kattis OJ
"""
best_c, best_s = 0, 0

for c in range(1, 6):
    vals = input()
    s = sum(map(int, vals.split()))
    if s > best_s:
        best_c, best_s = c, s

print(f"{best_c} {best_s}")