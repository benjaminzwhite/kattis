# Reverse Rot
# https://open.kattis.com/problems/reverserot
# TAGS: cipher
# CP4: 1.6k, Cipher, Easier
# NOTES:
"""
Simple trick: if you x2/double the lookup alphabet string, you can handle the indexing easily.

(Fast performance is not needed so can do repeated index(c) calls O_o)
"""
ALPH = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_." * 2

while True:
    ns = input()
    if ns == '0':
        break
    n, s = ns.split()

    n = int(n)

    res = ''.join(ALPH[ALPH.index(c) + n] for c in s[::-1])
    print(res)