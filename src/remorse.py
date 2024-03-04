# ReMorse
# https://open.kattis.com/problems/remorse
# TAGS: cipher, code, greedy
# CP4: 3.4a, Greedy (Classical)
# NOTES:
"""
Just find the most commonly occuring/highest frequency chars then assign them the lowest possible Morse score.
You can precompute the Morse scores by generating all strings of - and . until you have the 26 lowest possible values.

See code below, the exercise says that the score of a Morse letter is the symbols 3:- and 1:. PLUS 1 for each gap BETWEEN symbols
e.g. the Morse symbol "-." has a - for 3 points a gap for 1 point and a . for 1 point = 5 points

The res ALSO INCLUDES 3 * (len(s)-1) since each gap BETWEEN LETTERS is a space which also costs 3 points.
"""
from collections import Counter

# Generate all possible Morse code symbols until you have the 26 smallest values
# NOTE: the scores below *INCLUDE* the contribution due to gaps between symbols
# e.g. "-." has a score of 3 + 1 + 1 = 5 due to 1 gap between - and .
#      "---" has a score of 3+1+3+1+3 = 11 due to the 2 gaps etc.
REF = [1, 3, 3, 5, 5, 5, 7, 7, 7, 7, 7, 9, 9, 9, 9, 9, 9, 9, 9, 11, 11, 11, 11, 11, 11, 11]

x = input()

s = ''.join(c.upper() for c in x if c.isalpha())

c = Counter(s)

descending_frequencies = [t[1] for t in c.most_common()] # we want the frequencies in MOST_COMMON order to pair them with the LOWEST scores in REF

res = 3 * (len(s) - 1) + sum(r * freq for r, freq in zip(REF, descending_frequencies))

print(res)