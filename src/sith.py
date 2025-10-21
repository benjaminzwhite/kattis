# Sith
# https://open.kattis.com/problems/sith
# TAGS: basic
# CP4: 1.4d, Selection Only, 3+ Cases
# NOTES:
input()

a = int(input())
b = int(input())
c = int(input())

c_ = a - b
if c_ < 0 and c_ == c:
    print("JEDI")
elif c_ < 0 and c_ == -c:
    print("SITH")
else:
    print("VEIT EKKI")