# Esej
# https://open.kattis.com/problems/esej
# TAGS: set, random
# CP4: 2.3d, Hash Table (set)
# NOTES:
"""
IMHO the A,B stuff is unclear: it says A<=B and to generate between A and B words
but it wants you to generate at least B/2 distinct words so in reality the limit is the max of A and B//2+1
e.g. if A,B = 19,19 you need to either generate A=19 or B//2+1 = 10 words, so generate 19.
"""
import random

MAX_L = 5 # we'll generate words of at most 5 letters for time limit
# 26**5 = 11_881_376 so easily > 100_000 which is max needed words

ALPH = "abcdefghijklmnopqrstuvwxyz"

A, B = map(int, input().split())
LIMIT = max(A, (B // 2) + 1)

words = set()

while len(words) < LIMIT:
    random_word = ''.join(random.choices(ALPH, k=MAX_L))
    words.add(random_word)
    
print(' '.join(words))