# Prerequisites?
# https://open.kattis.com/problems/prerequisites
# TAGS: array
# CP4: 1.4i, Still Easy
# NOTES:
while True:
    km = input()
    if km == '0':
        break

    k, m = map(int, km.split())

    chosen = set(input().split())

    flg = False
    for _ in range(m):
        c, r, *xs = input().split()
        if sum(x in chosen for x in xs) < int(r):
            flg = True

    if not flg:
        print("yes")
    else:
        print("no")