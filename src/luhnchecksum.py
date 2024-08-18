# Luhn's Checksum Algorithm
# https://open.kattis.com/problems/luhnchecksum
# TAGS: array
# CP4: 1.6f, Real Life, Medium
# NOTES:
T = int(input())

for _ in range(T):
    s = input()
    luhn_sum = sum(sum(int(x) for x in str((1 + i % 2) * int(d))) for i, d in enumerate(s[::-1]))
    if luhn_sum % 10 == 0:
        print("PASS")
    else:
        print("FAIL")