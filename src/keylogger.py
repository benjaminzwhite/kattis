# Keylogger
# https://open.kattis.com/problems/keylogger
# TAGS: interpreter
# CP4: 1.6l, Cipher, Medium
# NOTES:
"""
Easy implementation if you XOR the uppercase state 0->1/1->0 to toggle between upper and lowercase

Also, added "spacebar" = "whack" = ' ' command to the d dictionary
"""
d = {'whack': ' ', 'clank': 'a', 'bong': 'b', 'click': 'c', 'tap': 'd', 'poing': 'e', 'clonk': 'f', 'clack': 'g', 'ping': 'h', 'tip': 'i', 'cloing': 'j', 'tic': 'k', 'cling': 'l', 'bing': 'm', 'pong': 'n', 'clang': 'o', 'pang': 'p', 'clong': 'q', 'tac': 'r', 'boing': 's', 'boink': 't', 'cloink': 'u', 'rattle': 'v', 'clock': 'w', 'toc': 'x', 'clink': 'y', 'tuc': 'z'}
res = []
uppercase = 0

N = int(input())

for _ in range(N):
    c = input()
    if c in ['bump', 'dink', 'thumb']:
        uppercase ^= 1
    elif c == 'pop':
        if res:res.pop()
    else:
        if uppercase:
            tmp = d[c].upper()
        else:
            tmp = d[c]
        res.append(tmp)

print(''.join(res))