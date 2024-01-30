# Tri
# https://open.kattis.com/problems/tri
# TAGS: brute force, eval
# CP4: 3.2h, Math Simulation, Easier
# NOTES:
a, b, c = input().split()

for o in "+-/*":
    if eval(a + o + b) == float(c):
        print(a + o + b + '=' + c)
        break
    elif eval(b + o + c) == float(a):
        print(a + '=' + b + o + c)
        break