# Drunk Vigenere
# https://open.kattis.com/problems/drunkvigenere
# TAGS: basic, cipher
# CP4: 1.6k, Cipher, Easier
# NOTES:
enc = input()
key = input()

dec = []

for i in range(len(enc)):
    tmp = (ord(enc[i]) - ord(key[i])) % 26
    tmp2 = (ord(enc[i]) + ord(key[i])) % 26
    if i % 2 == 0:
        dec.append(chr(tmp + 65))
    else:
        dec.append(chr(tmp2 + 65))

print(''.join(dec))