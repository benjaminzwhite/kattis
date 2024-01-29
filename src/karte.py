# Karte
# https://open.kattis.com/problems/karte
# TAGS: basic
# CP4: 1.6a, Game (Card)
# NOTES:
s = input()

cards = {s[i:i + 3] for i in range(0, len(s), 3)}

if len(cards) != len(s) // 3:
    print("GRESKA")
else:
    print(' '.join(str(13 - sum(x.startswith(c) for x in cards)) for c in "PKHT"))