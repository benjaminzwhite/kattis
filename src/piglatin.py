# Pig Latin
# https://open.kattis.com/problems/piglatin
# TAGS: cipher
# CP4: 1.6l, Cipher, Medium
# NOTES:
"""
CARE! y is a vowel here.
"""
from sys import stdin

VOWELS = {'a', 'e', 'i', 'o', 'u', 'y'}

def piglatin(word):
    if word[0] in VOWELS:
        return word + "yay"
    else:
        # input section says there is always at least one vowel in each word so no need to handle all-consonant case
        idx = next(i for i, c in enumerate(word) if c in VOWELS)
        res = word[idx:] + word[:idx] + "ay"
        return res

for line in stdin:
    res = ' '.join(piglatin(word) for word in line.split())
    print(res)