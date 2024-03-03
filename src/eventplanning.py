# Event Planning
# https://open.kattis.com/problems/eventplanning
# TAGS: basic
# CP4: 1.4i, Still Easy
# NOTES:
N, B, H, W = map(int, input().split())

best = B + 1

for _ in range(H):
    price = int(input())
    beds =  map(int, input().split())
    for bed in beds:
        if bed >= N and price * N < best:
            best = price * N

if best <= B:
    print(best)
else:
    print("stay home")