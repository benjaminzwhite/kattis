# Primary Arithmetic
# https://open.kattis.com/problems/primaryarithmetic
# TAGS: mathematics
# CP4: 2.2i, Big Integer
# NOTES:
"""
Basically same as simpleaddition, with a formatting requirement

(CARE! reading comprehension: plural vs singular 's' in operation's')
"""
from itertools import zip_longest

while True:
    A, B = input().split()
    if (A == '0' and B == '0'):
        break
    
    cnt = 0
    carry = 0
    
    for a, b in zip_longest(map(int, A[::-1]), map(int, B[::-1]), fillvalue=0):
        tmp = a + b + carry
        if tmp >= 10:
            cnt += 1
        carry, r = divmod(tmp, 10)
        
    print("{} carry operation{}.".format("No" if cnt == 0 else cnt, 's' if cnt > 1 else ''))