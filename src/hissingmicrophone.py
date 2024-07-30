# Hissing Microphone
# https://open.kattis.com/problems/hissingmicrophone
# TAGS: basic, array
# CP4: 1.4h, Easy
# NOTES:
st = input()

print("hiss" if any(l == r == 's' for l, r in zip(st, st[1:])) else "no hiss")