# Veður - Lokaðar heiðar
# https://open.kattis.com/problems/vedurheidar
# TAGS: basic
# CP4: 1.4f, Multiple TC + Selection
# NOTES:
v_max = int(input())

T = int(input())

for _ in range(T):
    name, v = input().split()
    if v_max > int(v):
        print(name, "lokud")
    else:
        print(name, "opin")