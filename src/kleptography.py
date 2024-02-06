# Kleptography
# https://open.kattis.com/problems/kleptography
# TAGS: cipher
# CP4: 6.2a, Cipher, Harder
# NOTES:
"""
I found this more difficult that the 1.6 Easy rating would suggest O_o

Took a while to understand what was being asked; so there might be a clearer solution approach.
"""
n, m = map(int, input().split())
peek = input()
ciphertext = input()

res = [' ' for _ in range(m - n)] + [*peek]

for i in range(m - 1, n - 1, -1):
    tmp = (ord(ciphertext[i]) - ord(res[i])) % 26
    res[i - n] = chr(97 + tmp)

print(''.join(res))