# ICPC
# https://open.kattis.com/problems/icpcawards
# TAGS: basic
# CP4: 2.3d, Hash Table (set)
# NOTES:
N = int(input())

prizes = 0
d = set()

for _ in range(N):
    if prizes >= 12:
        break
    winner = input()
    uni, team = winner.split()
    if uni not in d:
        d.add(uni)
        print(winner)
        prizes += 1