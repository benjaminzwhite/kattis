# Encoded Message
# https://open.kattis.com/problems/encodedmessage
# TAGS: array, cipher
# CP4: 1.6k, Cipher, Easier
# NOTES:
T = int(input())

for _ in range(T):
    s = input()
    N = int(len(s) ** 0.5)
    res = ''.join(s[i - j]  for j in range(N) for i in range(N - 1, N * N, N))
    print(res)