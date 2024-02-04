# Saving For Retirement
# https://open.kattis.com/problems/savingforretirement
# TAGS: basic, mathematics
# CP4: 3.2g, Try All Answers
# NOTES:
"""
Don't need to brute force, can solve analytically.

Also, reading comprehension:
It wants strictly greater than the target amount to match so just add +1 to formula
"""
from math import ceil

a, b, c, d, e = map(int, input().split())

target = (b - a) * c + 1 # IT WANTS STRICTLY GREATER THAN, hence +1

needed_years = ceil(target / e)

res = d + needed_years

print(res)