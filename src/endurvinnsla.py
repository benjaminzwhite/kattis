# Endurvinnsla
# https://open.kattis.com/problems/endurvinnsla
# TAGS: basic
# CP4: 1.5f, Easy, Involving String
# NOTES:
name = input()
pc = float(input())
n = int(input())

nonplastic = 0
for _ in range(n):
    tmp = input()
    if tmp == "ekki plast":
        nonplastic += 1

if nonplastic <= pc * n:
    print("Jebb")
else:
    print("Neibb")