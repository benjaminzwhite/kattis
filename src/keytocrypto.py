# The Key to Cryptography
# https://open.kattis.com/problems/keytocrypto
# TAGS: basic, string
# CP4: 1.6k, Cipher, Easier
# NOTES:
"""
Basically a ROT kind of thing - CARE! key can be LONGER than ciphertext so have to handle that case

Implemented below separately for clarity, can make it DRYer if you want
"""
ciph = input()
key = input()

ALPH = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

message = []
for i in range(min(len(key), len(ciph))): # key can be LONGER than ciphertext!!!
    idx = ALPH.index(ciph[i]) - ALPH.index(key[i])
    if idx < 0:
        idx += 26
    message.append(ALPH[idx])

if len(ciph) > len(key): # key can be LONGER than ciphertext!!!
    for j in range(len(key), len(ciph)):
        idx = ALPH.index(ciph[j]) - ALPH.index(message[j - len(key)])
        if idx < 0:
            idx += 26
        message.append(ALPH[idx])

print(''.join(message))