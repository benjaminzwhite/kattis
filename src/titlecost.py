# Title Cost
# https://open.kattis.com/problems/titlecost
# TAGS: basic
# CP4: 1.4a, I/O + Sequences Only
# NOTES:
s, f = input().split()
f = float(f)

print(min(len(s), f))