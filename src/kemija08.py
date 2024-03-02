# Kemija
# https://open.kattis.com/problems/kemija08
# TAGS: cipher
# CP4: 1.6k, Cipher, Easier
# NOTES:
s = input()

res = []
i = 0

while i < len(s):
    res.append(s[i])
    if s[i] in "aeiou":
        i += 2
    i += 1

print(''.join(res))