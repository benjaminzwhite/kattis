# Adding Trouble
# https://open.kattis.com/problems/addingtrouble
# TAGS: basic
# CP4: 1.4c, Selection Only
# NOTES:
a, b, c = map(int, input().split())

if a + b == c:
    print("correct!")
else:
    print("wrong!")