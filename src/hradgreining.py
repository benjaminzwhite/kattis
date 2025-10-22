# Hraðgreining
# https://open.kattis.com/problems/hradgreining
# TAGS: basic
# CP4: 1.4c, Selection Only, 2 Cases
# NOTES:
s = input()

bad = "COV"

if bad in s:
    print("Veikur!")
else:
    print("Ekki veikur!")