# Playfair Cipher
# https://open.kattis.com/problems/playfair
# TAGS: array, cryptography
# CP4: 6.2a, Cipher, Harder
# NOTES:
"""
Just implement as told.

Some tricky stuff due to handling adjacent chars (YOU INSERT IN PLACE, so cant process pairwise
then handle at end - see code where i do s[i:i+2] then if 2nd char is missing or is same as
first, convert to 'x' then i-=1 to replicate "inserting x" at this location)

---

Note:

I realised after submit that dont need SEEN set, can just use D dict directly
since these are the chars you've added to dict
"""
from string import ascii_lowercase as ALPH

k = input() + ALPH

R, C = 0, 0
seen = set()
D = {}
E = {}
for c in k:
    if c.isalpha() and c != 'q' and c not in seen:
        seen.add(c)
        D[c] = (R, C)
        E[(R, C)] = c
        C += 1
        if C == 5:
            R += 1
            C = 0
            if R == 5:
                break

s = ''.join(input().split())

res = []

i = 0
while i < len(s):
    if i == len(s) - 1:
        s += 'x'
    fst, snd = s[i:i+2]
    if fst == snd:
        snd = 'x'
        i -= 1
    i += 2

    rf, cf = D[fst]
    rs, cs = D[snd]

    if rf == rs:
        fst_ = E[(rf, (cf + 1) % 5)]
        snd_ = E[(rs, (cs + 1) % 5)]
    elif cf == cs:
        fst_ = E[((rf + 1) % 5, cf)]
        snd_ = E[((rs + 1) % 5, cs)]
    else:
        fst_ = E[(rf, cs)]
        snd_ = E[(rs, cf)]

    res.extend([fst_, snd_])

print(''.join(map(str.upper, res)))