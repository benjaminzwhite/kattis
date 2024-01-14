# Sibice
# https://open.kattis.com/problems/sibice
# TAGS: geometry, basic
# CP4: 7.2a, Points
# NOTES:
N, W, H = map(int, input().split())

for _ in range(N):
    x = int(input())
    if x * x <= (W * W + H * H):
        print("DA")
    else:
        print("NE")