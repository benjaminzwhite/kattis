# Filip
# https://open.kattis.com/problems/filip
# TAGS: basic
# CP4: 1.4f, Function
# NOTES:
A, B = input().split()

A = int(A[::-1])
B = int(B[::-1])

print(A if A > B else B)