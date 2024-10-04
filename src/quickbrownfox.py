# Quick Brown Fox
# https://open.kattis.com/problems/quickbrownfox
# TAGS: set
# CP4: 2.3b, DAT, ASCII
# NOTES:
N = int(input())

ALPH = set("abcdefghijklmnopqrstuvwxyz")

for _ in range(N):
    s = input()
    res = ALPH.difference(set(filter(lambda x: x in ALPH, s.lower())))
    if len(res) == 0:
        print("pangram")
    else:
        print("missing " + ''.join(sorted(res)))