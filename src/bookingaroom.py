# Booking a Room
# https://open.kattis.com/problems/bookingaroom
# TAGS: array
# CP4: 2.3c, DAT, Others
# NOTES:
"""
Since only 100 rooms, can make a boolean array of size 100 and update that instead
"""
r, n = map(int, input().split())

seen = set()

for _ in range(n):
    seen.add(int(input()))

print(next((i for i in range(1, r+1) if i not in seen), "too late"))