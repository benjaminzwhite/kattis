# Cypher Decypher
# https://open.kattis.com/problems/cypherdecypher
# TAGS: string, cipher
# CP4: 1.5b, Cipher, Easier
# NOTES:
nums = list(map(int, input()))

T = int(input())
for _ in range(T):
    tmp = []
    for i, c in enumerate(input()):
        x = ord(c) - 65 # CARE! 65, not 64, he calls A the 0th letter of alphabet O_o
        x *= nums[i]
        x %= 26
        tmp.append(chr(x + 65))
    print(''.join(tmp))