# Erase Securely
# https://open.kattis.com/problems/erase
# TAGS: basic, array
# CP4: 2.2a, 1D Array, Medium
# NOTES:
N = int(input())

s1 = input()
s2 = input()

if all(abs(int(c1) - int(c2)) == N % 2 for c1, c2 in zip(s1, s2)):
    print("Deletion succeeded")
else:
    print("Deletion failed")