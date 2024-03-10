# Candle Box
# https://open.kattis.com/problems/candlebox
# TAGS: brute force
# CP4: 5.2e, Number Systems/Seqs
# NOTES:
D = int(input())
R = int(input())
T = int(input())

for ar in range(4, 1000 + 1):
    total_rita = ar * (ar - 1) // 2 - 6
    at = ar - D
    total_theo = at * (at - 1) // 2 - 3
    if total_rita + total_theo == R + T:
        print(R - total_rita)
        break