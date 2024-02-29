# Text Encryption
# https://open.kattis.com/problems/textencryption
# TAGS: cipher
# CP4: 6.2a, Cipher, Harder
# NOTES:
"""
Pre-create the encryped array of the correct length then just send each element to its correct index, 
it's straightforward after that: when you overshoot the enc list, go back to start but +=1 the starting
index (originally start left to right at idx 0 then next loop through at idx 1 etc.)
"""
while (n := int(input())):
    plain = input()
    plain = ''.join(plain.split()).upper()
    L = len(plain)
    enc = [' ' for _ in range(L)]
    start_i = 0
    curr = 0
    for c in plain:
        enc[curr] = c
        curr += n
        if curr >= L:
            start_i += 1
            curr = start_i
    print(''.join(enc))