# Digits
# https://open.kattis.com/problems/digits
# TAGS: basic
# CP4: 1.4f, Function
# NOTES:
while True:
    s = input()
    if s == "END":
        break
    i = 1
    while s != str(len(s)):
        i += 1
        s = str(len(s))
    print(i)