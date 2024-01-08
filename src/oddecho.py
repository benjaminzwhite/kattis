# Odd Echo
# https://open.kattis.com/problems/oddecho
# TAGS: basic
# CP4: 1.4e, Control Flow
# NOTES:
n = int(input())

for i in range(1, n+1):
    s = input()
    if i % 2 == 1:
        print(s)