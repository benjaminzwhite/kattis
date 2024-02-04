# Mult!
# https://open.kattis.com/problems/mult
# TAGS: basic
# CP4: 1.4h, Easy
# NOTES:
N = int(input())

fst = int(input())

flg = False

for _ in range(N - 1):
    curr = int(input())
    if flg:
        fst = curr
        flg = False
    elif curr % fst == 0:
        print(curr)
        flg = True