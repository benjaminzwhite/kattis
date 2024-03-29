# ASCII Figure Rotation
# https://open.kattis.com/problems/asciifigurerotation
# TAGS: array
# CP4: 6.2d, Output Formatting, H
# NOTES:
"""
Lots of formatting requirements O_o
"""
from itertools import zip_longest

first = True # need to print blank line between testcases

while True:
    n = int(input())
    if n == 0:
        break
    if not first:
        print()
    first = False
    board = [input() for _ in range(n)]
    res = [''.join('|' if c == '-' else '-' if c == '|' else c for c in col[::-1]) for col in zip_longest(*board, fillvalue=' ')]
    for row in res:
        print(row.rstrip())