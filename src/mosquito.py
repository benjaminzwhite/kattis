# Mosquito Multiplication
# https://open.kattis.com/problems/mosquito
# TAGS: basic
# CP4: 1.4h, Easy
# NOTES:
import sys

for line in sys.stdin:
    M, P, L, E, R, S, N = map(int, line.split())

    for _ in range(N):
        L, P, M = M * E, L // R, P // S
    
    print(M)