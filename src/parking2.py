# Parking
# https://open.kattis.com/problems/parking2
# TAGS: brute force
# CP4: 3.2g, Try All Answers
# NOTES:
T = int(input())

for _ in range(T):
    n = int(input())
    xs = list(map(int, input().split()))
    print(2 * (max(xs) - min(xs)))