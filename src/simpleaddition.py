# Simple Addition
# https://open.kattis.com/problems/simpleaddition
# TAGS: mathematics
# CP4: 2.2i, Big Integer
# NOTES:
from itertools import zip_longest

A = input()
B = input()

res = []
carry = 0

for a, b in zip_longest(map(int, A[::-1]), map(int, B[::-1]), fillvalue=0):
    tmp = a + b + carry
    carry, r = divmod(tmp, 10)
    res.append(r)
    
if carry != 0:
    res.append(carry)
    
print(''.join(map(str, res[::-1])))