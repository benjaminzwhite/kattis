# Zebras and Ocelots
# https://open.kattis.com/problems/zebrasocelots
# TAGS: binary
# CP4: 2.2h, Bit Manipulation
# NOTES:
"""
The process mimics repeatedly adding +1 in binary, final state is 111....11111 of length==N, so 2**N-1 is final
"""
N = int(input())

xs = []
for _ in range(N):
    s = input()
    if s == 'Z':
        xs.append('1')
    else:
        xs.append('0')
        
print(2**N - int(''.join(xs), 2) - 1)