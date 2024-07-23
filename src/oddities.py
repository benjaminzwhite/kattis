# Oddities
# https://open.kattis.com/problems/oddities
# TAGS: basic
# CP4: 1.4d, Multiple TC + Selection
# NOTES:
n = int(input())

for _ in range(n):
    x = int(input())
    if x % 2:
        print(f"{x} is odd")
    else:
        print(f"{x} is even")