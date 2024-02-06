# iBoard
# https://open.kattis.com/problems/iboard
# TAGS: binary, array
# CP4: 2.2h, Bit Manipulation
# NOTES:
"""
Note: you get WA if you don't zfill to length 7 (I couldn't get sample tests to work until I realised this)
"""
while True:
    try:
        s = input()
        presses = ''.join(bin(x)[2:].zfill(7)[::-1] for x in map(ord, s)) # may need to rstrip the input to avoid newline char ?

        l, r = 0, 0

        for c in presses:
            if c == '0':
                r += 1
            else:
                l += 1

        if l % 2 == 0 and r % 2 == 0:
            print("free")
        else:
            print("trapped")
    except EOFError:
        break