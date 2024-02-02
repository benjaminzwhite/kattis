# Bottled-Up Feelings
# https://open.kattis.com/problems/bottledup
# TAGS: basic, mathematics
# CP4: 1.4j, Medium
# NOTES:
s, v1, v2 = map(int, input().split())

min_sum = float("inf")
best_a, best_b = -1, -1

for a in range(s // v1 + 1):
    remaining_v = s - a * v1
    if remaining_v % v2 == 0:
        b = remaining_v // v2
        if a + b < min_sum:
            best_a, best_b = a, b

if (best_a, best_b) == (-1, -1):
    print("Impossible")
else:
    print(best_a, best_b)