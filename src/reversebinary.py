# Reversed Binary Numbers
# https://open.kattis.com/problems/reversebinary
# TAGS: basic, binary
# CP4: 2.2j, Stack
# NOTES:
N = int(input())

print(int(bin(N)[2:][::-1], 2))