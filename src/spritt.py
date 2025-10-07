# Spritt
# https://open.kattis.com/problems/spritt
# TAGS: basic
# CP4: 1.4g, Control Flow, Level 1
# NOTES:
n, avail = map(int, input().split())

needed = 0

for _ in range(n):
    needed += int(input())
    
if avail >= needed:
    print("Jebb")
else:
    print("Neibb")