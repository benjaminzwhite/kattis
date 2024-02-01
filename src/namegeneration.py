# Name Generation
# https://open.kattis.com/problems/namegeneration
# TAGS: logic
# CP4: 9.cons, Construction
# NOTES:
"""
In principle this approach can fail because I didn't bother to set() the list.
The probability of generating 2 identical names is small though, and I was feeling lucky:
-> this was AC first try O_o
"""
from random import sample

for _ in range(int(input())):
    name = []
    for _ in range(6):
        name.extend(sample("bcdfghjklmnpqrstvwxyz", 2))
        name.extend(sample("aeiou", 1))
    print(''.join(name))