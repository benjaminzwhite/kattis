# Bus
# https://open.kattis.com/problems/bus
# TAGS: basic, string
# CP4: 5.2f, Log, Exp, Pow
# NOTES:
T = int(input())

for _ in range(T):
    k = int(input())
    print(2**k - 1)