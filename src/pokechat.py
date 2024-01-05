# Pokechat
# https://open.kattis.com/problems/pokechat
# TAGS: basic
# CP4: 1.4g, 1D Array, Easier
# NOTES:
alph = input()
code = input()

res = ''.join(alph[int(code[i:i+3]) - 1] for i in range(0, len(code), 3))

print(res)