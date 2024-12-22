# Good Messages
# https://open.kattis.com/problems/goodmessages
# TAGS: cipher
# CP4: 6.2a, Cipher, Harder
# NOTES:
"""
Some frustrating design/description reading comprehension mainly:

First, 'y' is a vowel here.

Second, the >, >=, <, <=, are written in english and using words that vary and have different interpretations:

1) "However, Boris does not does not like seeing messages that contain at least half as many vowels as consonants after applying an encoding step."
2) "Output ‘Boris’ if strictly more steps sound good than bad, and ‘Colleague’ otherwise."

So after talking about "BAD" messages, you should actually think about 1) in terms of GOOD messages - after trying all possible interpretations, it actually means:

- a string is "GOOD" if the count of vowels ('aeiouy') is strictly less than < (consonants) / 2

-> So, increment a good_counter by +=1 each time you apply the caesar cipher step

And 2) means:

result is "boris" if GOOD_COUNTER > BAD_COUNTER, which is equivalent to GOOD > (ALL - GOOD) where ALL is the N_times you do the encoding
"""
from string import ascii_lowercase as alph

d = {c:i for i, c in enumerate(alph)}

LOOKUP = alph + alph

def do_one_enc(s):
    return ''.join(LOOKUP[offset + d[c]] for c in s)

offset = int(input())

s = input()

N_times = int(input())

goods = 0
for _ in range(N_times):
    s = do_one_enc(s)
    vowels = sum(c in 'aeiouy' for c in s) # NOTE y IS A VOWEL
    if vowels < (len(s) - vowels) / 2: # bad practice, should check 2*vowels < len(s) - vowels, or 3*vowels < len(s)
        goods += 1

if goods > N_times // 2:
    print("Boris")
else:
    print("Colleague")