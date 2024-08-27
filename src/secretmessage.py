# Secret Message
# https://open.kattis.com/problems/secretmessage
# TAGS: cipher
# CP4: 1.6l, Cipher, Medium
# NOTES:
from math import ceil, sqrt

T = int(input())

for _ in range(T):
    s = input()
    L = len(s)
    K = ceil(sqrt(L))
    M = K**2
    
    s = s + (M - L) * '*'
    
    res = ''.join(curr_char for j in range(K, 0, -1) for i in range(K * K, 0, -K) if (curr_char := s[i - j]) != '*')
    
    print(res)