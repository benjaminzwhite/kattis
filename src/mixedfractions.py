# Primality
# https://open.kattis.com/problems/primality
# TAGS: mathematics
# CP4: 5.2i, Fractions
# NOTES:
while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    else:
        print(f"{a // b} {a % b} / {b}")