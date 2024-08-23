# Cryptographer's Conundrum
# https://open.kattis.com/problems/conundrum
# TAGS: array, cipher
# CP4: 1.6k, Cipher, Easier
# NOTES:
from itertools import cycle

it = cycle("PER")

s = input()

res = sum(1 for l, r in zip(it, s) if l != r)

print(res)