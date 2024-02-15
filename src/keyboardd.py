# Keyboardd
# https://open.kattis.com/problems/keyboardd
# TAGS: counter
# CP4: 2.3b, DAT, ASCII
# NOTES:
from collections import Counter

s1 = input()
s2 = input()

c1 = Counter(s1)
c2 = Counter(s2)

res = [k for k, v in c2.items() if v == 2 * c1[k]]

print(''.join(res))