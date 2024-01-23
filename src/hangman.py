# Hangman
# https://open.kattis.com/problems/hangman
# TAGS: string
# CP4: 6.4a, String Matching
# NOTES:
s = input()
g = input()

guesses = 10
i = 0
S = set(s)

while guesses > 0:
    if g[i] in S:
        S.remove(g[i])
        if len(S) == 0:
            break
    else:
        guesses -= 1
    i += 1

if guesses > 0:
    print("WIN")
else:
    print("LOSE")