# Jumbo Javelin
# https://open.kattis.com/problems/jumbojavelin
# TAGS: basic
# CP4: 1.4b, Repetition Only
# NOTES:
"""
- didn't understand the multiline input format, was first day on Kattis
"""
n = int(input())

s = 0

for _ in range(n):
    x = int(input())
    s += x

print(s - n + 1)