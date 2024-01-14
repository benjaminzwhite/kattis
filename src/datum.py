# Datum
# https://open.kattis.com/problems/datum
# TAGS: basic, datetime
# CP4: 1.6h, Time, Easier
# NOTES:
"""
- can use Python datetime/calendar libraries if you like importing O_o
- can use Zeller's congruence if you want to read a bit online
"""
D, M = map(int, input().split())

days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
names = ["Wednesday", "Thursday", "Friday", "Saturday", "Sunday", "Monday", "Tuesday"]
idx = (D + sum(days[:M])) % 7

print(names[idx])