# Rhyme Power aka Rimstyrka
# https://open.kattis.com/problems/rimstyrka
# TAGS: string, sorting
# CP4: 0, Not In List Yet
# NOTES:
"""
Very similar / used this approach recently for:
https://open.kattis.com/problems/znanstvenik
See solution for the above exercise znanstvenik.py

Basically sort by lexicographic order (here the twist is the words are backwards since comparing suffixes)
then adjacent words in the sorted lists have similar "suffixes" (i.e. "prefixes" in the backwards list O_o confusing)
"""
n = int(input())

backwards_words = []
for _ in range(n):
    backwards_words.append(input()[::-1])

backwards_words = sorted(backwards_words)

best = 0
for w1, w2 in zip(backwards_words, backwards_words[1:]):
    curr = 0
    for c1, c2 in zip(w1, w2):
        if c1 == c2:
            curr += 1
        else:
            break
    if curr < min(len(w1), len(w2)): # CARE! not allowed for 1 word to be entirely contained within other eg teapot vs pot will have score 3 but not allowed
        # not a suffix of the other so valid case:
        best = max(best, curr)

print(best)